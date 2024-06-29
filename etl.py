from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://vscode:password@localhost:5432/airbnb')

df = pd.read_sql('SELECT * FROM airbnb_raw', engine)

df['date'] = pd.to_datetime(df['last_review']).dt.date
df['time'] = pd.to_datetime(df['last_review']).dt.time
df['avg_price_neighborhood'] = df.groupby('neighbourhood')['price'].transform('mean')
df.fillna({'reviews_per_month': 0}, inplace=True)

df_transformed = df[['id', 'name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 
                     'latitude', 'longitude', 'room_type', 'price', 'minimum_nights', 
                     'number_of_reviews', 'date', 'time', 'reviews_per_month', 
                     'calculated_host_listings_count', 'availability_365', 'avg_price_neighborhood']]

df_transformed.to_sql('airbnb_transformed', engine, if_exists='replace', index=False)
