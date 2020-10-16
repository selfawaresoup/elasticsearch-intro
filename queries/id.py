#!/usr/bin/python3

import sqlite3

sql = sqlite3.connect('data.db')
for row in sql.execute('''
  select *
  from questions
  where
    id = 135711
  '''):
  print(row)