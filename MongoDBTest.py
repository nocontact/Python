from pymongo import MongoClient
import pymongo

client = MongoClient()
db = client.test
cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"}).sort([
    ("borough", pymongo.ASCENDING),
    ("address.zipcode", pymongo.ASCENDING)
])
for document in cursor:
    print(document)