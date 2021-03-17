def process_200(balance_sheets, code, index):
    data_cols = list()

    for comp in balance_sheets:
        data_col = list()

        if code == '200' or code == '201' or code == '202':
            for k in range(5):
                try:
                    data = round((comp.loc[index][k] / comp.loc['Total Equity'][k]), 2)
                    data_col.append(data)
                except IndexError:
                    data_col.insert(0, 0.0)

        elif code == '203':
            for k in range(5):
                try:
                    data = round((comp.loc[index][k] / comp.loc['Total Current Liabilities'][k]), 2)
                    data_col.append(data)
                except IndexError:
                    data_col.insert(0, 0.0)

        data_cols.append(data_col)

    return data_cols
