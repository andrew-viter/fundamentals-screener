import subprocess
import json
import pandas as pd
import chart_generation as cg
import file_system_ops as fso
from datetime import date
from chart_generation.validate_symbols import validate_symbols

def generate_chart():
    with open('../config/config.json') as config_file:
        config_data = json.load(config_file)
        r_script_path = config_data["r_script_executable_path"]
        r_files_directory = config_data["r_files_directory"]

    symbols = cg.collect_input(cg.vms.vsymbol, "Symbol entry mode", len_compare=True)
    invalid_symbols = validate_symbols(symbols)
    for i in invalid_symbols:
        symbols.remove(i)
    
    income_statements = cg.collect_data(symbols, '')
    balance_sheets = cg.collect_data(symbols, 'balance-sheet')
    cash_flows = cg.collect_data(symbols, 'cash-flow')

    year = date.today().year
    last_5_cal_years = list()
    for l in range(5):
        last_5_cal_years.append((year - 5) + l)

    datafr = pd.DataFrame(index=last_5_cal_years, columns=symbols)

    datafr.to_csv(path_or_buf="C:/Users/andre/PythonProjects/fundamentals_screener/data/data.csv", index_label="year")

    args = "--vanilla"
    rfile_path = "\"{}/line_plot.R\"".format(r_files_directory)
    hidden = subprocess.DEVNULL
    subprocess.run(' '.join([r_script_path, args, rfile_path]), stdout=hidden, stderr=hidden)