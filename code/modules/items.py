from connectors.mongo_proxy import MongoProxy
import pandas as pd
import csv


class ItemsOperations:
    actions = []
    csv_path: str

    def __init__(self, db_connection, channel, action):
        self.db_connection: MongoProxy = db_connection
        self.channel = channel
        self.action = action
        self.csv_path = f"csv_data/items_{self.action}_data.csv"

    def perform(self):
        if self.action == "csv":
            return self.generate_csv()

        # return self[self.action]()

        print("[Items] action not found")

    def generate_csv(self):
        db_conn = self.db_connection
        results: list = db_conn["items"].find({})

        df: pd.DataFrame = pd.DataFrame(results)
        df.to_csv(self.csv_path, quoting=csv.QUOTE_ALL)
        print(f"file generated and available on path: {self.csv_path}")
