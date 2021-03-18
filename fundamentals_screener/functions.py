# necessary imports
import subprocess
import json
import os
import glob
import pandas as pd
import chart_generation as cg
from datetime import date
from shutil import copy

def chart_generation():
    # creates path strings for config data
    with open('../config/config.json') as config_file:
        config_data = json.load(config_file)
        r_script_path = config_data["r_script_executable_path"]
        r_files_directory = config_data["r_files_directory"]

    # deletes any old png files from the directory to prepare for new ones
    # subprocess.run("del ../*.png", shell=True)

    # runs the collection of symbols and their associated data
    symbols = cg.collect_input(cg.vms.vsymbol, "Symbol entry mode", len_compare=True)
    income_statements = cg.collect_data(symbols, '')
    balance_sheets = cg.collect_data(symbols, 'balance-sheet')
    cash_flows = cg.collect_data(symbols, 'cash-flow')

    codes = cg.collect_input(cg.vms.vcode, "Code entry mode")
    stringified_codes = list()
    for c in codes:
        stringified_codes.append(cg.dicts.indexes[c])

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
            cols_add = cg.hundred.one(income_statements, code, index)

        elif code[0] == '2':
            cols_add = cg.hundred.two(balance_sheets, code, index)
        
        elif code[0] == '3':
            cols_add = cg.hundred.three(cash_flows, code, index)

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
            "main title": cg.dicts.main_titles[code],
            "axis title": cg.dicts.axis_titles[code]
        }

        # dumps names specific to code iteration into a file
        with open('../data/data.json', 'w') as outfile:
            json.dump(datafr_specifics, outfile)

        print("Executing line_plot.R with code " + code)

        #runs the r script that produces a graph
        args = "--vanilla"
        rfile_path = "\"{}/line_plot.R\"".format(r_files_directory)
        hidden = subprocess.DEVNULL
        subprocess.run(' '.join([r_script_path, args, rfile_path]), stdout=hidden, stderr=hidden)

def image_cleanup():
    # list of all image files, if any
    image_file_paths = glob.glob("C:\\Users\\andre\\PythonProjects\\fundamentals_screener\\*.png")

    if len(image_file_paths) == 0:
        print("No images to cleanup")
    else:
        # removes each image file one by one, since wildcards do not work with os.remove()
        for image in image_file_paths:
            try:
                os.remove(image)
            except:
                print("Error while removing file: " + image)

def archive():
    # list of all image files, if any
    image_file_paths = glob.glob("C:\\Users\\andre\\PythonProjects\\fundamentals_screener\\*.png")

    if len(image_file_paths) == 0:
        print("No images to archive")
    else:
        with open('../config/config.json') as config_file:
            config_data = json.load(config_file)
            archive_path = config_data["png_archive_path"]
            
            if os.access(archive_path, os.F_OK):
                for image in image_file_paths:
                    copy(image, archive_path)

            else:
                print("The destination for \'archive\' does not seem to exist. Check archive path configuration in \'config.json\'")

