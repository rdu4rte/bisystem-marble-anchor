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
    users = self.db_connection['users'].find({})
