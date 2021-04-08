from pandas import read_html

# returns array of invalid symbols, to be removed by caller
def validate_symbols(syms):
    invalid_symbols = []

    for s in syms:
        try:
            _ = read_html(f'https://www.marketwatch.com/investing/stock/{s}/financials/', match='Item')
        except ValueError:
            invalid_symbols.append(s)
    
    return invalid_symbols