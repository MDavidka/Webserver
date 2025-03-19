from pymongo import MongoClient
from config import DB_URI

client = MongoClient(DB_URI)
db = client.spotify_tracker

def get_db():
    return db