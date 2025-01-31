### Are you unsatisfied of working with mock data in dev environment ?
MongoNow is here to help.
### Do you wonder if there is a quick way of setting up a dummy MongoDB instance in less that seconds?

With MongoNow, all your problems have finally found a solution. 
Install MongoNow with `pip` or `git` and your Mongo-like database
is ready to be used in seconds.

# Installation
Install the MongoNow package with python-pip or clone it from github.
#### Install using pip:
```shell
$ pip install mongonow
```

#### Install using git:
```shell
$ git clone https://github.com/AlexandreMahdhaoui/MongoNow.git
```

# Usage:

- Create a MongoNowClient instance and start exploring its content:
```python
from mongonow import MongoNowClient

# Create a MongoNowClient specifying the path of your databases.
client = MongoNowClient(path='/dbs')
# Select one of your database
db = client['test_db']
# Select a collection
cheese_collection = db['cheese']
```
- Perform a query on your collection with the same syntax you would use 
for MongoDB:
```python
# SELECT all FROM cheese documents WHERE price is less than 4.99 AND country is France
>>> cheese_collection.find({
....    '$and': [
....        {'$lt': {'price': '4.99'}},
....        {'$eq': {'country': 'France'}} # or {'country: 'France'} without $eq
....    ]
.... })

Iterator([
    {
        "_id": 5590198231212309,
        "name": "Camembert",
        "price": 2.99,
        "country": "France"
    },    
    {
        "_id": 5512398091283234,
        "name": "Maroilles",
        "price": 4.49,
        "country": "France"
    }
])
```
- Mutate several documents
```python
# Set field discounted to True for all french cheese
cheese_collection.update_many(
    {"country": "France"},
    {"discounted": True}
)
```

# File Structure

The structure of the local database should be conform to the MongoNow's
file structure Specification.
- The Database Container (e.g. `dbs/`) containing all databases.
The path of this folder has to be specified during MongoNowClient
instanciation: ``client = MongoNowClient(path='/dbs')``
- Database folders (e.g. `test_db/`) containing all its collection.
Navigate to this database with ``db = client['test_db']``.
- Collection files (e.g. ``cheese.json``): Navigate to this collection with `coll = db['cheese']`.


```json
...
└── dbs/
    ├── dev_db/
    │   └── ...
    └── test_db/
        ├── users.json
        │   └── ...
        └── cheese.json
            └── {
                  "cheese": [
                    {
                      "_id": 5590198231212309,
                      "name": "Camembert",
                      "price": 2.99,
                      "country": "France"
                    },
                    {
                      "_id": 5512398091283234,
                      "name": "Maroilles",
                      "price": 4.49,
                      "country": "France"
                    }
                  ]
                }
```