class SalesOperations:
    def __init__(self, db_connection, channel, action):
        self.db_connection = db_connection
        self.channel = channel
        self.action = action

    def perform(self):
        print(f"sales module, channel: {self.channel}, action: {self.action}")
        pass
