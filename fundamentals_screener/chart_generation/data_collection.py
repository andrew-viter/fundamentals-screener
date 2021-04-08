import pandas as pd
from decimal import Decimal
from chart_generation.dicts import mult_value

def collect_data(symbols, statement):
    # this is a list of bad symbols that need to be tossed
    # any invalid symbols are added to this list, and removed from the main one later
    # this avoids issues involved with modifying an iterable
    symbols_to_remove = list()

    cleaned_data_frames = list()

    for symbol in symbols:
        # url for webpage with financial data
        url = 'https://www.marketwatch.com/investing/stock/' + symbol + '/financials/' + statement
        
        # gets table, sets dataframe to proper table
        try:
            tables = pd.read_html(url,match='Item')
            print("Scraping " + url)
        except ValueError:
            print("Unable to access data at " + url)
            symbols_to_remove.append(symbol)
            continue
        finally:
            if len(tables) == 1:
                financials = tables[0]
            else:
                financials = pd.concat(tables)

        if statement == '':
            indexes_to_keep = ['Gross Income', 'Net Income', 'Cost of Goods Sold (COGS) incl. D&A', 'EPS (Basic)', 'Sales/Revenue']
        elif statement == 'balance-sheet':
            indexes_to_keep = ['Total Liabilities', 'Long-Term Debt', 'ST Debt & Current Portion LT Debt', 'Total Current Assets', 'Total Equity', 'Total Current Liabilities']
        elif statement == 'cash-flow':
            indexes_to_keep = ['Net Operating Cash Flow', 'Capital Expenditures']

        financials = drop_unneeded_columns(financials)
        financials = drop_unneeded_indexes(financials, indexes_to_keep)
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
    
    # takes care of permanently removing bad symbols from the list
    # this should only execute when collecting income statements
    for s in symbols_to_remove:
        symbols.remove(s)

    return cleaned_data_frames


def drop_unneeded_indexes(df, indexes):
    # temp stores all the indexes, regardless of if they are duplicate or not
    # indexes_to_delete has only one copy of each index
    temp = []
    indexes_to_delete = list()

    for i in df.index:
        if not i in indexes:
            temp.append(i)

    # uses list comprehension to only add once
    [indexes_to_delete.append(i) for i in temp if i not in temp]
    df.drop(index=indexes_to_delete)

    return df

def drop_unneeded_columns(df):
    df.drop(columns=['5-year trend'], inplace=True)
    df.rename(columns={'Item  Item':'Item'}, inplace=True)

    indexes = list()
    # iterates through each row, gets name, stores altered copy of name
    for _, row in df.iterrows():
        old_name = row['Item']
        new_length = (len(old_name) // 2 - 1)
        new_name = old_name[:new_length]
        indexes.append(new_name)   

    df.index = indexes
    df.drop(columns=['Item'], inplace=True)
    
    return df
