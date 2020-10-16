#!/usr/bin/python3
import requests

q = {
  "query": {
    "match": {
      "question": "europe moon france ocean"
    }
  }
}

r = requests.post('http://localhost:9200/questions/_search', json=q).json()

for hit in r['hits']['hits']:
  print(f"{hit['_score']} \t{hit['_source']['question']}")

print('---')
print(f"Total hits: {r['hits']['total']['value']}")