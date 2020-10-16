#!/usr/bin/python3
import requests

q = {
  "query": {
    "match_phrase": {
      "question": {
        "query": "sun moon earth",
        "slop": 8
      }
    }
  },
  "size": 100
}

r = requests.post('http://localhost:9200/questions/_search', json=q).json()


for hit in r['hits']['hits']:
  print(f"{hit['_score']} \t{hit['_source']['value']} \t{hit['_source']['question']}")

print('---')
print(f"Total hits: {r['hits']['total']['value']}")