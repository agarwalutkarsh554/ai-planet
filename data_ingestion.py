import pandas as pd
from sqlalchemy import create_engine

# Load dataset
df = pd.read_csv('AB_NYC_2019.csv')

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:password@localhost:5432/airbnb')

# Load data into table
df.to_sql('airbnb_data', engine, if_exists='replace', index=False)