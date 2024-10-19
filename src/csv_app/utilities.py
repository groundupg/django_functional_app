import pandas as pd
from django.http import HttpResponse
import io

def convert_into_df(csv_file) -> pd.DataFrame:
    df = pd.read_csv(csv_file)
    return df

def remove_duplicates(df:pd.DataFrame) -> pd.DataFrame:
    unduplicated_df = df.drop_duplicates()
    return unduplicated_df

def convert_df_to_csv(df:pd.DataFrame)-> None:
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=export.csv'
    return response