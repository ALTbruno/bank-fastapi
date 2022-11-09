from decouple import config
from pymongo import MongoClient
from bson import ObjectId
from dtos.CustomerSave import CustomerSave

from util.MongoDB import MongoDB
MongoDB.initialize()
customers_collection = MongoDB.DATABASE.customers

class CustomerRepository:

	def create(self, customer: CustomerSave):
		customer_id = customers_collection.insert_one(customer.__dict__).inserted_id
		created_customer = customers_collection.find_one({ '_id': customer_id })
		return created_customer

	def get_all(self):
		return customers_collection.find()

	def find_by_id(self, id: str):
		return customers_collection.find_one({ '_id': ObjectId(id) })

	def exists(self, customer: CustomerSave) -> bool:
		exists_by_cpf = customers_collection.count_documents({'cpf': customer.cpf}) > 0
		exists_by_email = customers_collection.count_documents({'email': customer.email}) > 0
		return exists_by_cpf or exists_by_email
