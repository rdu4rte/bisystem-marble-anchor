from faker import Faker
from pymongo import MongoClient
from connectors.mongodb import mongo_connection
from bson.objectid import ObjectId
import datetime

fake = Faker(['pt_BR'])


def seed():
  connection: MongoClient = mongo_connection()
  data: list = [
      {'collection': 'items', 'data': []},
      {'collection': 'sales', 'data': []},
      {'collection': 'users', 'data': []}
  ]

  for _ in range(10):
    id = ObjectId()
    item: dict = {
        '_id': id
    }

    data[0]['data'].append(item)

  for i in data:
    print('[Seed] Seeding collection {} - {}'.format(i['collection'], datetime.datetime.now()))
    connection[i['collection']].insert_many(i['data'])


seed()
print('[Seed] Data seeded - {}'.format(datetime.datetime.now()))
