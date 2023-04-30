from pymongo import MongoClient
import os
import json
from dotenv import load_dotenv
load_dotenv()


client = MongoClient(os.getenv('CONNECTION_STRING'))
db = client.E_Commerce
categories = os.listdir("E:\Mini-Project (Sem 4)\Database\Json")
print(categories)
for category in categories:
    print(category[0:-5])
    with open(f"E:\Mini-Project (Sem 4)\Database\Json\{category}" , "r") as f:
        collection = db[category[0:-5]]
        collection.insert_many((json.loads(f.read()))["product"])

