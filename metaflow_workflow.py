from metaflow import FlowSpec, step

class AirbnbETLFlow(FlowSpec):

    @step
    def start(self):
        print("ETL process started...")
        self.next(self.data_ingestion)

    @step
    def data_ingestion(self):
        import data_ingestion
        print("Data ingestion completed.")
        self.next(self.transformation)

    @step
    def transformation(self):
        import transformation
        print("ETL pipeline completed.")
        self.next(self.end)

    @step
    def end(self):
        print("ETL process completed successfully!")

if __name__ == '__main__':
    AirbnbETLFlow()