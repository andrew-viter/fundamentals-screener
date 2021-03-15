# necessary imports
import subprocess
import json
import pandas as pd
import dicts
from datetime import date
from symbol_input import collect_symbols
from data_collection import collect_data
from code_input import collect_codes

# deletes any old png files from the directory to prepare for new ones
subprocess.run("del *.png", shell=True)

symbols = collect_symbols()
income_statements = collect_data(symbols, '')
balance_sheets = collect_data(symbols, 'balance-sheet')
cash_flows = collect_data(symbols, 'cash-flow')

code_tuple = collect_codes()
stringified_codes = code_tuple[0]
codes = code_tuple[1]

# gets the current year, for consistency with differing fiscal years
year = date.today().year

# makes a list of last 5 calendar years, excl. current, to use for indices of dataframe
last_5_cal_years = list()
for l in range(5):
    last_5_cal_years.append((year - 5) + l)

# loops over each code in the list
for j in range(len(codes)):
    df_index = stringified_codes[j]
    code = codes[j]

    # makes the dataframe for storing data from code operation
    datafr = pd.DataFrame(index=last_5_cal_years, columns=symbols)
    cols_add = list()

    if code[0] == '1':
        # loops over the company first
        # this is necessary in the event that they have no data for one or more years
        # it allows for the insertion of 0 to the start of data
        for company in income_statements:
            col_add = list()

            # loops over last 5 years of data, or as many as available
            for k in range(5):
                # will try to add the data for a year
                try:
                    data = 100 * round((company.loc[df_index][k] / company.loc['Sales/Revenue'][k]), 4)
                    col_add.append(data)
                except IndexError:
                    # if index error (no data), add 0 to the front of list
                    col_add.insert(0, 0.0)
            
            # adds the data from company to data from all companies
            cols_add.append(col_add)

    # adds a column for each symbol, using the correct column data
    for symbol in symbols:
        datafr[symbol] = cols_add[symbols.index(symbol)]

    # the completed dataframe is added into the list of dataframes
    # dfs.append(datafr)

    # converts the dataframe into a csv file
    datafr.to_csv(path_or_buf="C:/Users/andre/PythonProjects/fundamentals_screener/data.csv", index_label="year")

    # dictionary to be converted to json
    datafr_specifics = {
        "code": code,
        "main title": dicts.main_titles[code],
        "axis title": dicts.axis_titles[code]
    }

    # dumps names specific to code iteration into a file
    with open('data.json', 'w') as outfile:
        json.dump(datafr_specifics, outfile)

    print("Executing line_plot_visualization.R with code " + code)

    #runs the r script that produces a graph
    subprocess.run("C:/Program Files/R/R-4.0.4/bin/Rscript.exe --vanilla \"C:/Users/andre/OneDrive/Documents/R Files/line_plot_visualization.R\"", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Done")