def process_100(income_statements, code, index):
    # stores the column of data for each company
    data_cols = list()

    for comp in income_statements:
        # all data is added into a column before being pushed into list
        data_col = list()

        # gross, net, and operating margins, respectively
        if code == '100' or code == '101' or code == '102':
            for k in range(5):
                # will try to add the data for a year
                try:
                    data = 100 * round((comp.loc[index][k] / comp.loc['Sales/Revenue'][k]), 4)
                    data_col.append(data)
                except IndexError:
                    # if index error (no data), add 0 to the front of list
                    data_col.insert(0, 0.0)

        # EPS
        elif code == '103':
            for k in range(5):
                try:
                    data_col.append(comp.loc[index][k])
                except IndexError:
                    data_col.insert(0, 0.0)

        # adds column of data from current company to other columns 
        data_cols.append(data_col)

    return data_cols

