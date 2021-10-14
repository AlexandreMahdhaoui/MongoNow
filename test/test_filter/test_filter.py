import json
import os

from mongonow.filter.filter import Filter


class TestFilter:
    def test_from_collection(self):
        with open(os.path.join('test', 'test_filter', 'test_filter.json')) as f:
            data = json.load(f)
        coll = data['collection']
        query = {
            '$or': [
                {'_id': 0},
                {'_id': {
                    '$gte': 2
                }}
            ]
        }
        print(Filter.from_collection(coll, query))
