from pymongo import MongoClient
from settings import DB_URL

#url = "mongodb://localhost:27017/myTestDB"
client = MongoClient(DB_URL)

db = client.library_db

events_collection = db["events"]
materials_collection = db["materials"]
users_collection = db["users"]

""" try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB")
except Exception as e:
    print(e) """
