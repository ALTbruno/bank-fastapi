from bson import ObjectId
from decouple import config
from pymongo import MongoClient
from models.TransferModel import TransferModel

MONGODB_URL = config("MONGODB_URL")

mongo_client = MongoClient(MONGODB_URL)
database = mongo_client.bank_fastapi
transfers_collection = database.transfers

class TransferRepository:

    def create(self, transfer: TransferModel):
        transfer_id = transfers_collection.insert_one(transfer.__dict__).inserted_id
        created_transfer = transfers_collection.find_one({ '_id': ObjectId(transfer_id) })
        return created_transfer

    def get_by_account(self, account_id: str):
        return transfers_collection.find({
            "$or": [
            {'origin_account_id': account_id},
            {'destination_account_id': account_id}
            ]
        }).sort('datetime', -1)