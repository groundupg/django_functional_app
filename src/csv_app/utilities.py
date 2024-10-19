import pandas as pd

def convert_into_df(csv_file) -> pd.DataFrame:
    df = pd.read_csv(csv_file)
    return df

def remove_duplicates(df:pd.DataFrame) -> pd.DataFrame:
    unduplicated_df = df.drop_duplicates()
    return unduplicated_df

def convert_df_to_csv(df:pd.DataFrame)-> None:
    csv = df.to_csv()
    return csv