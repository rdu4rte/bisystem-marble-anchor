from pymongo import MongoClient
import pandas as pd
import csv
import datetime


class ItemsOperations:
  actions = ['items_category_analysis', 'items_by_category']

  def __init__(self, db_connection, channel, action):
    self.db_connection: MongoClient = db_connection
    self.channel = channel
    self.action = action

  def perform(self):
    if self.action in self.actions and self.action == self.actions[0]:
      return self.items_category_analysis()
    if self.action in self.actions and self.action == self.actions[1]:
      return self.items_by_category()

    print('[Items] action not found')

  def items_category_analysis(self):
    items = self.db_connection['items'].find({})
    df = pd.DataFrame(items).sort_values(by='category', ascending=True)
    df.to_csv(f'csv_data/{self.action}.csv')
    return {}

  def items_by_category(self):
    items = self.db_connection['items'].find({})

    results: list = []
    items_count = len(list(items.clone()))
    progress: int = 1

    categories: list = [
        {'category': 'internal', 'amount': 0},
        {'category': 'external', 'amount': 0},
        {'category': 'hybrid', 'amount': 0}
    ]

    for item in items:
      print(f'[{progress}/{items_count}] item: {item["name"]}, int: {categories[0]["amount"]} / ext: {categories[1]["amount"]} / hyb: {categories[2]["amount"]}')

      if item['category'] == 'internal':
        categories[0]["amount"] += 1
      elif item['category'] == 'external':
        categories[1]["amount"] += 1
      elif item['category'] == 'hybrid':
        categories[2]["amount"] += 1

      results.append({
          'name': item['name'],
          'category': item['category']
      })

      progress += 1

    print(pd.DataFrame(categories).sort_values(by='amount', ascending=False))
