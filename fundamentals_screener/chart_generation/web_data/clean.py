from decimal import Decimal
import pandas as pd

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

def clean_table_data(df):
    final_data = []
    for _, data_list in df.iterrows():
        clean_data_list = []
        for data in data_list:
            if data == '-':
                data = 0
            
            if '(' or ')' in str(data):
                # str(data) IS necessary, otherwise it breaks
                data = str(data).replace('(', '-')
                data = data.replace(')', '')

            if ',' in data:
                data = data.replace(',', '')

            suffix = data[-1]

            if suffix == '%' or suffix.isdigit():
                data = data.replace('%', '')
                data = Decimal(data)

            else:
                data = data.replace(suffix, '')
                multiplier = {
                                'K': 1000,
                                'M': 1000000,
                                'B': 1000000000
                            }[suffix]
                data = (Decimal(data) * multiplier)
            
            clean_data_list.append(data)
        final_data.append(clean_data_list)
    return pd.DataFrame(final_data, index=df.index, columns=df.columns)
