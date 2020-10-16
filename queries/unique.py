#!/usr/bin/python3

import sqlite3

sql = sqlite3.connect('data.db')
for row in sql.execute('''
  select category, count(*) as c
  from questions
  where
    value > 200
  group by category
  order by c desc
  limit 8;
  '''):
  print(row)
