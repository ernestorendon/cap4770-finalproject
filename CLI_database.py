import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_PASSWORD')
dbname = os.getenv('MONGO_DBNAME')

# Construct the connection string
connection_string = f"mongodb+srv://{username}:{password}@cluster0.mwlsdbh.mongodb.net/{dbname}?retryWrites=true&w=majority"
client = MongoClient(connection_string)

db = client['World_Cup_Predictor']
collection = db['matches']  

result = collection.find_one({"home_team": "England", "away_team": "Scotland"})
print(result)
