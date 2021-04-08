import pandas as pd
from chart_generation.clean_web_data import drop_useless_columns, drop_useless_indexes, clean_table_data
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
                clean_data = clean_table_data(data)
                cleaned_data.append(clean_data)

            # adds list of cleaned values to list of all values
            final_data.append(cleaned_data)

        # creates a new dataframe with cleaned data, retains index and column names
        df_new = pd.DataFrame(final_data, index=financials.index, columns=financials.columns)

        # adds cleaned dataframe to list
        cleaned_data_frames.append(df_new)

    return cleaned_data_frames
