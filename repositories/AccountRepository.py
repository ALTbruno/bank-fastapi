from hashlib import new
from decouple import config
from pymongo import MongoClient, ReturnDocument
from bson import ObjectId

from models.AccountModel import AccountModel

MONGODB_URL = config("MONGODB_URL")

mongo_client = MongoClient(MONGODB_URL)
database = mongo_client.bank_fastapi
accounts_collection = database.accounts

class AccountRepository:
	
	def create(self, account: AccountModel):
		account_id = accounts_collection.insert_one(account.__dict__).inserted_id
		created_account = accounts_collection.find_one({ '_id': ObjectId(account_id)})
		return created_account

	def get_all(self):
		return accounts_collection.find()

	def find_by_id(self, id: str):
		return accounts_collection.find_one({ '_id': ObjectId(id)})

	def update_balance(self, id: str, new_balance: int):
		account = accounts_collection.find_one_and_update(
			{'_id': id},
			{'$set': {'balance': new_balance}},
			return_document=ReturnDocument.AFTER
		)
		return account
		
	def exists(self, account_number: str) -> bool:
		return accounts_collection.count_documents({'account_number': account_number}) > 0
