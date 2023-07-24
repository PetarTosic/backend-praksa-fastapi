from pymongo import MongoClient
from config.settings import mongodb_uri, port

client = MongoClient(mongodb_uri, port)
db = client['TestDB']

