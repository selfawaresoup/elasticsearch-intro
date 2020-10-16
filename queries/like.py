#!/usr/bin/python3

import sqlite3

sql = sqlite3.connect('data.db')
for row in sql.execute('''
  select *
  from questions
  where
    question LIKE "%europe%"
    AND question LIKE "%moon%"
    AND question LIKE "%france%"
    AND question LIKE "%ocean%"
  '''):
  print(row)