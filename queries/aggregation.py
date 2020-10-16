#!/usr/bin/python3
import requests
import pprint

pp = pprint.PrettyPrinter(indent=2)

q = {
  "query": {
    "match_all": {
    }
  },
  "aggs": {
    "categories": {
      "terms": {
        "field": "category.keyword",
        "size": 8
      }
    }
  }
}

r = requests.post('http://localhost:9200/questions/_search', json=q)
pp.pprint(r.json()['aggregations'])