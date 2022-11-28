import pandas as pd
import csv
import datetime


class UsersOperations:
  actions = ['users_analysis']

  def __init__(self, db_connection, channel, action):
    self.db_connection: MongoClient = db_connection
    self.channel = channel
    self.action = action

  def perform(self):
    if self.action in self.actions and self.action == self.actions[0]:
      return self.users_analysis()

    print('[Users] action not found')

  def users_analysis(self):
    metrics: list = [
        {'status': 'active', 'amount': 0},
        {'status': 'inactive', 'amount': 0}
    ]

    users = self.db_connection['users'].find({})

    for user in users:
      if user['active']:
        metrics[0]['amount'] += 1
      elif not user['active']:
        metrics[1]['amount'] += 1

    df = pd.DataFrame(metrics).sort_values(by='status', ascending=False)
    print(df)
