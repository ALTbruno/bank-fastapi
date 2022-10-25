from decouple import config
from pymongo import MongoClient
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
		accounts = []
		for account in accounts_collection.find():
			accounts.append(self.convert_to_account_find(account))
		return accounts

	def find_by_id(self, id: str):
		account = accounts_collection.find_one({ '_id': ObjectId(id)})
		return self.convert_to_account_find(account)

	def convert_to_account_find(self, account):
		return {
			'id': str(account['_id']),
			'agency_number': str(account['agency_number']),
			'account_number': str(account['account_number']),
			'balance': str(account['balance']),
			'customer_id': str(account['customer_id'])
		}
		
	def exists(self, account_number: str) -> bool:
		return accounts_collection.count_documents({'account_number': account_number}) > 0
