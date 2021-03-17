# necessary imports
import subprocess
import json
import pandas as pd
import dicts
from datetime import date
from collect_input import collect_input
from data_collection import collect_data
import validation_methods as vms
import one_hundred
import two_hundred
import three_hundred

# creates path strings for config data
with open('config/config.json') as config_file:
    config_data = json.load(config_file)
    rscript_path = config_data["r_script_executable_path"]
    r_files_directory = config_data["r_files_directory"]

# deletes any old png files from the directory to prepare for new ones
subprocess.run("del *.png", shell=True)

# runs the collection of symbols and their associated data
symbols = collect_input(vms.vsymbol, len_compare=True)
income_statements = collect_data(symbols, '')
balance_sheets = collect_data(symbols, 'balance-sheet')
cash_flows = collect_data(symbols, 'cash-flow')

codes = collect_input(vms.vcode)
stringified_codes = list()
for c in codes:
    stringified_codes.append(dicts.indexes[c])

# gets the current year, for consistency with differing fiscal years
year = date.today().year

# makes a list of last 5 calendar years, excl. current, to use for indices of dataframe
last_5_cal_years = list()
for l in range(5):
    last_5_cal_years.append((year - 5) + l)

# loops over each code in the list
for j in range(len(codes)):
    code = codes[j]
    index = stringified_codes[j]

    # makes the dataframe for storing data from code operation
    datafr = pd.DataFrame(index=last_5_cal_years, columns=symbols)
    cols_add = list()

    if code[0] == '1':
        cols_add = one_hundred.process_100(income_statements, code, index)

    elif code[0] == '2':
        cols_add = two_hundred.process_200(balance_sheets, code, index)
    
    elif code[0] == '3':
        cols_add = three_hundred.process_300(cash_flows, code, index)

    # adds a column for each symbol, using the correct column data
    for symbol in symbols:
        datafr[symbol] = cols_add[symbols.index(symbol)]

    # the completed dataframe is added into the list of dataframes
    # dfs.append(datafr)

    # converts the dataframe into a csv file
    datafr.to_csv(path_or_buf="C:/Users/andre/PythonProjects/fundamentals_screener/data/data.csv", index_label="year")

    # dictionary to be converted to json
    datafr_specifics = {
        "code": code,
        "main title": dicts.main_titles[code],
        "axis title": dicts.axis_titles[code]
    }

    # dumps names specific to code iteration into a file
    with open('data/data.json', 'w') as outfile:
        json.dump(datafr_specifics, outfile)

    print("Executing line_plot.R with code " + code)

    #runs the r script that produces a graph
    args = "--vanilla"
    rfile_path = "\"{}/line_plot.R\"".format(r_files_directory)
    hidden = subprocess.DEVNULL
    subprocess.run(' '.join([rscript_path, args, rfile_path]), stdout=hidden, stderr=hidden)

print("Done")