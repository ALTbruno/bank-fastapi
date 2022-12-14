from bson import ObjectId
from dtos.CustomerSave import CustomerSave
from exceptions.BusinessException import BusinessException
from repositories.CustomerRepository import CustomerRepository
from services.AccountService import AccountService

customerRepository = CustomerRepository()
accountService = AccountService()

class CustomerService:

	def create(self, customer: CustomerSave):
		if customerRepository.exists(customer):
			raise BusinessException(400, "Usuário já cadastrado")

		created_customer = customerRepository.create(customer)
		# * deixar assim? ou fazer via contaRepository?
		customer_id = str(created_customer['_id'])
		accountService.create(customer_id)
		return self.convert_to_customer_find(created_customer)

	def get_all(self):
		customers = []
		for customer in customerRepository.get_all():
			customers.append(self.convert_to_customer_find(customer))
		return customers

	def find_by_id(self, id: str):
		customer = customerRepository.find_by_id(id)
		return self.convert_to_customer_find(customer)

	def convert_to_customer_find(self, customer):
		return {
			'id': str(customer['_id']),
			'name':  str(customer['name']),
			'last_name': str(customer['last_name']),
			'cpf': str(customer['cpf']),
			'email': str(customer['email'])
		}