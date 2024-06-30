from sqlalchemy import create_engine
import pandas as pd

# Create a SQLAlchemy engine to connect to the PostgreSQL database
engine = create_engine('postgresql://postgres:password@localhost/airbnb')

# Data Extraction
listings_query = "SELECT * FROM listings"
calendar_query = "SELECT * FROM calendar"
listings_df = pd.read_sql_query(listings_query, engine)
calendar_df = pd.read_sql_query(calendar_query, engine)

# Data Transformation
# Normalize data (e.g., separate date and time into different columns)
listings_df['listing_date'] = pd.to_datetime(listings_df['last_review'])
listings_df['listing_time'] = listings_df['listing_date'].dt.time
listings_df.drop('last_review', axis=1, inplace=True)

# Calculate additional metrics (e.g., average price per neighborhood)
avg_price_per_neighborhood = listings_df.groupby('neighbourhood_group')['price'].mean().reset_index()

# Handle missing values (e.g., fill, remove, or flag them)
listings_df['description'] = listings_df['description'].fillna('No description provided')

# Data Loading
transformed_listings_df = listings_df[['id', 'listing_date', 'listing_time', 'neighbourhood_group', 'price', 'description']]
transformed_listings_df.to_sql('transformed_listings', engine, if_exists='replace', index=False)
avg_price_per_neighborhood.to_sql('avg_price_per_neighborhood', engine, if_exists='replace', index=False)