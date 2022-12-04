from pymongo import MongoClient


class UsersOperations:
    actions = []

    def __init__(self, db_connection, channel, action):
        self.db_connection: MongoClient = db_connection
        self.channel = channel
        self.action = action

    def perform(self):
        print("[Users] action not found")
