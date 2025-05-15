import pandas as pd
from pymongo import MongoClient
import certifi

uri = "mongodb+srv://shumankr99:sSuAAWNasR6aIhkr@cluster0.zngrhkq.mongodb.net/"

client = MongoClient(uri, tls=True, tlsCAFile=certifi.where())

db = client['shopDB']
collection = db['products']

df = pd.read_csv('products.csv')

collection.delete_many({})

collection.insert_many(df.to_dict(orient='records'))

print("✅ Data uploaded successfully to MongoDB Atlas")
