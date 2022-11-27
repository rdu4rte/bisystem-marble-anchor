from faker import Faker
from pymongo import MongoClient
from connectors.mongodb import mongo_connection
from bson.objectid import ObjectId
import numpy as np
import datetime
import random

fake = Faker(['pt_BR'])


def seed():
  connection: MongoClient = mongo_connection()
  data: list = [
      {'collection': 'items', 'data': []},
      {'collection': 'sales', 'data': []},
      {'collection': 'users', 'data': []}
  ]

  item_ids: list = []
  user_ids: list = []

  # items
  for _ in range(250):
    id = ObjectId()
    item: dict = {
        '_id': id,
        'name': fake.word(),
        'category': fake.random_element(
            elements=('internal', 'external', 'hybrid')),
        'description': fake.paragraph(nb_sentences=1),
        'active': True,
        'created_at': datetime.datetime.now(),
        'updated_at': datetime.datetime.now()
    }

    item_ids.append(id)
    data[0]['data'].append(item)

  # users
  for _ in range(200):
    id = ObjectId()
    first_name = fake.first_name()
    last_name = fake.last_name()

    item: dict = {
        '_id': id,
        'email': '{}_{}@{}'.format(first_name.lower(), last_name.lower(), fake.free_email_domain()),
        'firstname': first_name,
        'lastname': last_name,
        'created_at': datetime.datetime.now(),
        'updated_at': datetime.datetime.now()
    }

    user_ids.append(id)
    data[2]['data'].append(item)

  # sales
  for _ in range(100):
    id = ObjectId()
    value: float = np.random.uniform(100, 1000)
    amount: int = random.randint(1, 8)

    item: dict = {
        '_id': id,
        'user_id': fake.random_element(elements=user_ids),
        'value': f'{value:5.2f}',
        'status': fake.random_element(elements=['done', 'in_progress', 'canceled', 'paused']),
        'items': list(np.random.choice(item_ids, size=amount))
    }

    data[1]['data'].append(item)

  for i in data:
    print('[Seed] Seeding collection {} - {}'.format(i['collection'], datetime.datetime.now()))
    connection[i['collection']].insert_many(i['data'])


seed()
print('[Seed] Data seeded - {}'.format(datetime.datetime.now()))
