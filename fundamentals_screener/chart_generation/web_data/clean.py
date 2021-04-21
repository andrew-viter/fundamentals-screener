from decimal import Decimal

def drop_useless_indexes(df, indexes):
    indexes_to_delete = []

    for i in df.index:
        if not i in indexes or indexes_to_delete:
            indexes_to_delete.append(i)

    df.drop(index=indexes_to_delete)

    return df

def drop_useless_columns(df):
    df.drop(columns=['5-year trend'], inplace=True)
    df.rename(columns={'Item  Item':'Item'}, inplace=True)

    indexes = list()
    for _, row in df.iterrows():
        old_name = row['Item']
        new_length = (len(old_name) // 2 - 1)
        new_name = old_name[:new_length]
        indexes.append(new_name)   

    df.index = indexes
    df.drop(columns=['Item'], inplace=True)
    
    return df

def clean_table_data(val):
    if val == '-':
        return 0
    
    if '(' or ')' in val:
        val = val.replace('(', '-')
        val = val.replace(')', '')

    if ',' in val:
        val = val.replace(',', '')

    suffix = val[-1]

    if suffix == '%' or suffix.isdigit():
        val = val.replace('%', '')
        return Decimal(val)

    else:
        val = val.replace(suffix, '')
        multiplier = {
                        'K': 1000,
                        'M': 1000000,
                        'B': 1000000000
                     }[suffix]
        return Decimal(val) * multiplier
