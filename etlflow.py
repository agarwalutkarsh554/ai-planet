from metaflow import FlowSpec, step
from sqlalchemy import create_engine
import pandas as pd

class ETLFlow(FlowSpec):

    @step
    def start(self):
        self.next(self.ingest_data)

    @step
    def ingest_data(self):
        self.df = pd.read_csv('AB_NYC_2019.csv')
        self.next(self.transform_data)

    @step
    def transform_data(self):
        self.df['date'] = pd.to_datetime(self.df['last_review']).dt.date
        self.df['time'] = pd.to_datetime(self.df['last_review']).dt.time
        self.df['avg_price_neighborhood'] = self.df.groupby('neighbourhood')['price'].transform('mean')
        self.df.fillna({'reviews_per_month': 0}, inplace=True)

        self.df_transformed = self.df[['id', 'name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 
                                       'latitude', 'longitude', 'room_type', 'price', 'minimum_nights', 
                                       'number_of_reviews', 'date', 'time', 'reviews_per_month', 
                                       'calculated_host_listings_count', 'availability_365', 'avg_price_neighborhood']]
        self.next(self.load_data)

    @step
    def load_data(self):
        engine = create_engine('postgresql://vscode:password@localhost:5432/airbnb')
        self.df_transformed.to_sql('airbnb_transformed', engine, if_exists='replace', index=False)
        self.next(self.end)

    @step
    def end(self):
        print("ETL workflow completed")

if __name__ == '__main__':
    ETLFlow()
