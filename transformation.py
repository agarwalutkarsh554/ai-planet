import pandas as pd
from sqlalchemy import create_engine

# Load dataset

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:password@localhost:5432/airbnb')
df = pd.read_sql_query("SELECT * FROM public.airbnb_data", engine)

# Normalize date column
df['date'] = pd.to_datetime(df['last_review']).dt.date
df['time'] = pd.to_datetime(df['last_review']).dt.time

# Calculate average price per neighborhood
avg_price = df.groupby('neighbourhood')['price'].mean().reset_index()
avg_price.columns = ['neighbourhood', 'avg_price']

# Handle missing values
df.fillna({'reviews_per_month': 0}, inplace=True)
avg_price.to_sql('avg_price', engine, if_exists='replace', index=False)
