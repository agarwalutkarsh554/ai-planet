import pandas as pd
from sqlalchemy import create_engine

# Read the CSV file(s) into pandas DataFrames
listings_df = pd.read_csv('listings.csv')
calendar_df = pd.read_csv('calendar.csv')

# Create a SQLAlchemy engine to connect to the PostgreSQL database
engine = create_engine('postgresql://postgres:password@localhost/airbnb')

# Create a table with an appropriate schema
listings_df.to_sql('listings', engine, if_exists='replace', index=False)
calendar_df.to_sql('calendar', engine, if_exists='replace', index=False)