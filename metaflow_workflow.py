import metaflow

from metaflow import FlowSpec, step
metaflow.disable_plugin('kubernetes')
metaflow.disable_plugin('batch')

class AirbnbETLFlow(FlowSpec):

    @step
    def start(self):
        print("ETL process started...")
        self.next(self.data_ingestion)

    @step
    def data_ingestion(self):
        import data_ingestion
        print("Data ingestion completed.")
        self.next(self.etl_pipeline)

    @step
    def etl_pipeline(self):
        import etl_pipeline
        print("ETL pipeline completed.")
        self.next(self.end)

    @step
    def end(self):
        print("ETL process completed successfully!")

if __name__ == '__main__':
    AirbnbETLFlow()