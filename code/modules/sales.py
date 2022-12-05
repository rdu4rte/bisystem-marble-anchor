from connectors.mongo_proxy import MongoProxy
import pandas as pd
import csv


class SalesOperations:
    actions = []
    csv_path: str

    def __init__(self, db_connection, action, module):
        self.db_connection: MongoProxy = db_connection
        self.action = action
        self.module = module
        self.csv_path = f"csv_data/{module}_{action}_data.csv"

    def perform(self):
        self.generate_csv()
        return self[self.action]()

    def generate_csv(self):
        db_conn = self.db_connection
        results: list = db_conn[self.module].find({})

        df: pd.DataFrame = pd.DataFrame(results)
        df.to_csv(self.csv_path, quoting=csv.QUOTE_ALL)
        print(
            f"[{self.module}] file generated and available on path:",
            f"{self.csv_path}",
        )
