import pandas as pd
import chart_generation.web_data.clean as clean
import chart_generation.web_data.source as source

def collect_data(symbols, statement):
    cleaned_data_frames = list()

    for symbol in symbols:
        financials = source.source_data(symbol, statement)
        financials = clean.drop_useless_columns(financials)

        final_data = list()

        for _, raw_data_list in financials.iterrows():
            cleaned_data = list()

            for data in raw_data_list:
                clean_data = clean.clean_table_data(data)
                cleaned_data.append(clean_data)

            final_data.append(cleaned_data)

        df_new = pd.DataFrame(final_data, index=financials.index, columns=financials.columns)

        cleaned_data_frames.append(df_new)

    return cleaned_data_frames
