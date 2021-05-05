from pandas import read_html, concat

def source_data(symbol, statement):
    # url for webpage with financial data
    url = 'https://www.marketwatch.com/investing/stock/' + symbol + '/financials/' + statement
        
    # gets table, sets dataframe to proper table
    tables = read_html(url,match='Item')
    if len(tables) == 1:
        fi = tables[0]
    else:
        fi = concat(tables)

    return fi