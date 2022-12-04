from connectors.mongo_proxy import MongoProxy
from pymongo import MongoClient
from config.env import mongo_uri, mongo_db


def mongo_connection(db_name=None) -> MongoProxy:
    client: MongoClient = MongoClient(mongo_uri)
    return MongoProxy(conn=client)[db_name or mongo_db]
