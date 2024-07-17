# scripts/mongo_connection.py
import os
from dotenv import load_dotenv
from pymongo import MongoClient

def get_mongo_client():
    # Load environment variables from .env file
    load_dotenv()

    username = os.getenv('MONGO_USERNAME')
    password = os.getenv('MONGO_PASSWORD')
    dbname = os.getenv('MONGO_DBNAME')

    connection_string = f"mongodb+srv://{username}:{password}@cluster0.mwlsdbh.mongodb.net/{dbname}?retryWrites=true&w=majority"
    client = MongoClient(connection_string)
    return client

def get_matches_collection():
    client = get_mongo_client()
    db = client[os.getenv('MONGO_DBNAME')]
    return db['matches']
