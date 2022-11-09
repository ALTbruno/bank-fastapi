from decouple import config
from pymongo import MongoClient

class MongoDB:
    URI = config("MONGODB_URL")
    DATABASE = None

    @staticmethod
    def initialize():
        client = MongoClient(MongoDB.URI)
        MongoDB.DATABASE = client[config("DATABASE")]
