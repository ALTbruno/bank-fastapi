from random import randrange
from models.AccountModel import AccountModel

from repositories.AccountRepository import AccountRepository

accountRepository = AccountRepository()

class AccountService:
	
	def generate_number(self):
		return str(randrange(1000000000, 9000000000))

	def create(self, customer_id: str):
		account_number = self.generate_number()
		while accountRepository.exists(account_number):
			account_number = self.generate_number()
		account = AccountModel(agency_number = '0001', account_number = account_number, balance = 0, customer_id = customer_id)
		return accountRepository.create(account)

	def get_all(self):
		return accountRepository.get_all()
