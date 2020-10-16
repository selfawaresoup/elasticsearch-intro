#!/usr/bin/python3
import requests

q = {
  "query": {
    "fuzzy": {
      "question": {
        "value": "euorth"
      }
    }
  },
  "size": 30
}

r = requests.post('http://localhost:9200/questions/_search', json=q).json()

for hit in r['hits']['hits']:
  print(f"{hit['_score']} \t{hit['_source']['question']}")

print('---')
print(f"Total hits: {r['hits']['total']['value']}")