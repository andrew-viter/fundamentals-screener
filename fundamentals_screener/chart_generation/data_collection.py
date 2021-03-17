import pandas as pd
from dicts import mult_value

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
            if statement == '':
                financials = tables[0]
            else:
                financials = pd.concat(tables)

        financials = financials.drop(columns=['5-year trend'])
        financials = financials.rename(columns={'Item  Item':'Item'})
        indexes = list()

        # iterates through each row, gets name, stores altered copy of name
        for index, row in financials.iterrows():
            old_name = row['Item']
            new_length = int((len(old_name) / 2) - 1)
            index_name = old_name[0:new_length]
            indexes.append(index_name)

        financials.index = indexes
        financials = financials.drop(columns=['Item'])
        final_data = list()

        # cleans up the string data and converts it into numeric form
        for index, raw_data_list in financials.iterrows():

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
                elif ',' in data:
                    data = data.replace(',', '')

                suffix = data[len(data) - 1]

                # processes suffix and applies appropriate precision
                if suffix == '%':
                    data = data.replace('%', '')
                    cleaned_data.append(round(float(data), 2))
                    continue
                elif suffix.isdigit():
                    cleaned_data.append(round(float(data), 2))
                    continue
                elif not suffix.isdigit():
                    mult = suffix
                    data = data.replace(mult, '')
                    multiplier = mult_value[mult]
                    numeric_data = float(data)
                    cleaned_data.append(round(numeric_data * multiplier))

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
