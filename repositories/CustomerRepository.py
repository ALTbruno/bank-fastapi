from decouple import config
from pymongo import MongoClient
from bson import ObjectId
from dtos.CustomerSave import CustomerSave

MONGODB_URL = config("MONGODB_URL")

mongo_client = MongoClient(MONGODB_URL)
database = mongo_client.bank_fastapi
customers_collection = database.customers

class CustomerRepository:

	def convert_to_customer_find(self, customer):
		return {
			'id': str(customer['_id']),
			'name':  str(customer['name']),
			'last_name': str(customer['last_name']),
			'cpf': str(customer['cpf']),
			'email': str(customer['email'])
		}

	def create(self, customer: CustomerSave):
		customer_id = customers_collection.insert_one(customer.__dict__).inserted_id
		created_customer = customers_collection.find_one({ '_id': customer_id })
		return self.convert_to_customer_find(created_customer)

	def get_all(self):
		customers = []
		for customer in customers_collection.find():
			customers.append(self.convert_to_customer_find(customer))

		return customers

	def find_by_id(self, id: str):
		customer = customers_collection.find_one({ '_id': ObjectId(id) })
		return self.convert_to_customer_find(customer)

	def exists(self, customer: CustomerSave) -> bool:
		exists_by_cpf = customers_collection.count_documents({'cpf': customer.cpf}) > 0
		exists_by_email = customers_collection.count_documents({'email': customer.email}) > 0
		return exists_by_cpf or exists_by_email