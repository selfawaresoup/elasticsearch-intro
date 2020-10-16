#!/usr/bin/python3

import sqlite3

sql = sqlite3.connect('data.db')
for row in sql.execute('''
  select *
  from questions
  where
    question LIKE "%europe%"
    OR question LIKE "%moon%"
    OR question LIKE "%france%"
    OR question LIKE "%ocean%"
  '''):
  print(row[2])