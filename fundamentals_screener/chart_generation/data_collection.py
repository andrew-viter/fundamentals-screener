import pandas as pd
from decimal import Decimal
from chart_generation.dicts import mult_value
from chart_generation.web_data_cleaner import drop_useless_columns, drop_useless_indexes
from chart_generation.source_web_data import source_data

def collect_data(symbols, statement):
    cleaned_data_frames = list()

    for symbol in symbols:
        financials = source_data(symbol, statement)

        if statement == '':
            indexes_to_keep = ['Gross Income', 'Net Income', 'Cost of Goods Sold (COGS) incl. D&A', 'EPS (Basic)', 'Sales/Revenue']
        elif statement == 'balance-sheet':
            indexes_to_keep = ['Total Liabilities', 'Long-Term Debt', 'ST Debt & Current Portion LT Debt', 'Total Current Assets', 'Total Equity', 'Total Current Liabilities']
        elif statement == 'cash-flow':
            indexes_to_keep = ['Net Operating Cash Flow', 'Capital Expenditures']

        financials = drop_useless_columns(financials)
        financials = drop_useless_indexes(financials, indexes_to_keep)
        final_data = list()

        # cleans up the string data and converts it into numeric form
        for _, raw_data_list in financials.iterrows():

            # temporary list for storing the row's cleaned values
            cleaned_data = list()

            for data in raw_data_list:

                # no data, set it to 0
                if data == '-':
                    cleaned_data.append(0)
                    continue
                
                # parentheses value, remove them and set negative
                elif data[0] == '(':
                    data = data.replace('(', '-')
                    data = data.replace(')', '')

                # gets rid of any commas, which can interfere with float conversion
                if ',' in data:
                    data = data.replace(',', '')

                suffix = data[-1]

                # processes suffix and applies appropriate precision
                if suffix == '%':
                    data = data.replace('%', '')
                    cleaned_data.append(Decimal(data))
                    continue
                elif suffix.isdigit():
                    cleaned_data.append(Decimal(data))
                    continue
                elif not suffix.isdigit():
                    mult = suffix
                    data = data.replace(mult, '')
                    multiplier = mult_value[mult]
                    numeric_data = Decimal(data)
                    cleaned_data.append(numeric_data * multiplier)

            # adds list of cleaned values to list of all values
            final_data.append(cleaned_data)

        # creates a new dataframe with cleaned data, retains index and column names
        df_new = pd.DataFrame(final_data, index=financials.index, columns=financials.columns)

        # adds cleaned dataframe to list
        cleaned_data_frames.append(df_new)

    return cleaned_data_frames
