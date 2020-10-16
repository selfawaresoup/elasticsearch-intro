#!/usr/bin/python3
import sqlite3
import json
import requests


# CREATE SQLITE DATABASE

sql = sqlite3.connect('data.db')
sql.execute('DROP TABLE IF EXISTS questions;')
sql.execute('''
CREATE TABLE questions
  (
    id integer not null primary key,
    air_date date,
    category text,
    question text,
    answer text,
    round text,
    value integer,
    show_number integer
  );''')
sql.commit()

# CREATE ES INDEX

ES_URL = 'http://localhost:9200'
INDEX_URL = f"{ES_URL}/questions"

with open('mapping.json') as mapping_file:
  mapping = json.load(mapping_file)
  r = requests.get(INDEX_URL)
  if r.status_code == 200:
    requests.delete(INDEX_URL)
  requests.put(INDEX_URL, json=mapping)

# FILL DATA

bulk_es_body = ""

with open('data.json') as json_file:
  data = json.load(json_file)
  for i, q in enumerate(data):
    if isinstance(q['value'], str):
      q['value'] = int(q['value'].replace(',', '').replace('$', ''))
    record = (i, q['air_date'], q['category'], q['question'], q['answer'], q['round'], q['value'], q['show_number'])
    sql.execute('INSERT INTO questions VALUES (?, ?, ?, ?, ?, ?, ?, ?)', record)
    bulk_es_body += '{"index": { "_index": "questions", "_id": "%i" } }\n%s\n'%(i, json.dumps(q))

sql.commit()
print('SQlite: Stored %i records.'%(len(data)))
# print(bulk_es_body)
r = requests.post(f"{ES_URL}/_bulk", data=bulk_es_body, headers={"Content-Type": "application/x-ndjson"})
#print(r.json())
