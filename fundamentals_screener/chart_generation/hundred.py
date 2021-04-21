def one(income_statements, code, index):
    data_cols = list()

    for comp in income_statements:
        data_col = list()

        if code in ('101', '102', '103'):
            for k in range(5):
                try:
                    data = 100 * round((comp.loc[index][k] / comp.loc['Sales/Revenue'][k]), 4)
                    data_col.append(data)
                except IndexError:
                    data_col.insert(0, 0.0)

        elif code == '103':
            for k in range(5):
                try:
                    data_col.append(comp.loc[index][k])
                except IndexError:
                    data_col.insert(0, 0.0)

        data_cols.append(data_col)

    return data_cols

def two(balance_sheets, code, index):
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

def three(cash_flows, code, index):
    data_cols = list()

    for comp in cash_flows:
        data_col = list()

        if code == '300':
            for k in range(5):
                try:
                    data = (comp.loc[index][k] - abs(comp.loc['Capital Expenditures'][k]))
                    data_col.append(data)
                except IndexError:
                    data_col.insert(0, 0.0)

        data_cols.append(data_col)

    return data_cols