from dtos.CustomerSave import CustomerSave
from repositories.CustomerRepository import CustomerRepository
from services.AccountService import AccountService

customerRepository = CustomerRepository()
accountService = AccountService()

class CustomerService:
	def create(self, customer: CustomerSave):
		try:
			exists = customerRepository.exists(customer)
			if exists:
				return None
			else:
				customer = customerRepository.create(customer)
				# * deixar assim? ou fazer via contaRepository?
				accountService.create(customer['id'])
				return customer
		except Exception as ex:
			raise(ex)

	def get_all(self):
		return customerRepository.get_all()

	def find_by_id(self, id: str):
		return customerRepository.find_by_id(id)