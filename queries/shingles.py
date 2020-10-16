#!/usr/bin/python3
import requests

phrase = "sun moon earth"

q = {
  "query": {
    "bool": {
      "must": {
        "match": {
          "question": phrase
        }
      },
      "should": [
        {
          "match": {
            "question.shingles": "sun moon earth"
          }
        }
      ]
    }

  }
}

r = requests.post('http://localhost:9200/questions/_search', json=q).json()

for hit in r['hits']['hits']:
  print(f"{hit['_score']} \t{hit['_source']['question']}")

print('---')
print(f"Total hits: {r['hits']['total']['value']}")