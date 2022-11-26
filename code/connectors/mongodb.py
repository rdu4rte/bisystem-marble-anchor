from pymongo import MongoClient
from config.env import mongo_uri, mongo_db


def mongo_connection(db_name=None):
  client: MongoClient = MongoClient(mongo_uri)
  return client[db_name or mongo_db]
