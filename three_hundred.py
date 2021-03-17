def process_300(cash_flows, code, index):
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