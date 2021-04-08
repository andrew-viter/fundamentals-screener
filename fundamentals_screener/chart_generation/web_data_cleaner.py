def drop_useless_indexes(df, indexes):
    # indexes_to_delete keeps only one copy of each index
    indexes_to_delete = []

    for i in df.index:
        if not i in indexes or indexes_to_delete:
            indexes_to_delete.append(i)

    # uses list comprehension to only add once
    df.drop(index=indexes_to_delete)

    return df

def drop_useless_columns(df):
    df.drop(columns=['5-year trend'], inplace=True)
    df.rename(columns={'Item  Item':'Item'}, inplace=True)

    indexes = list()
    # iterates through each row, gets name, stores altered copy of name
    for _, row in df.iterrows():
        old_name = row['Item']
        new_length = (len(old_name) // 2 - 1)
        new_name = old_name[:new_length]
        indexes.append(new_name)   

    df.index = indexes
    df.drop(columns=['Item'], inplace=True)
    
    return df
