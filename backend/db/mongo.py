# db/mongo.py

from pymongo import MongoClient

def get_collection():
    # MongoDB connection string with correct database and collection
    client = MongoClient("mongodb+srv://shumankr99:sSuAAWNasR6aIhkr@cluster0.zngrhkq.mongodb.net/")
    db = client['shopDB']  # 'shopDB' is your database
    collection = db['products']  # 'products' is the collection name
    return collection
