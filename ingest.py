import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('AB_NYC_2019.csv')
engine = create_engine('postgresql://vscode:password@localhost:5432/airbnb')

df.to_sql('airbnb_raw', engine, if_exists='replace', index=False)
