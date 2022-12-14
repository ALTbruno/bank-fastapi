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
		accounts = []
		for account in accountRepository.get_all():
			accounts.append(self.convert_to_account_find(account))
		return accounts

	def find_by_id(self, id: str):
		account = accountRepository.find_by_id(id)
		return self.convert_to_account_find(account)

	def get_balance(self, id: str):
		account = self.find_by_id(id)
		return {"balance": account['balance']}

	def convert_to_account_find(self, account):
		return {
			'id': str(account['_id']),
			'agency_number': str(account['agency_number']),
			'account_number': str(account['account_number']),
			'balance': str(account['balance']),
			'customer_id': str(account['customer_id'])
		}
	
	def update_balance(self, account_id: str, new_balance: int):
		return accountRepository.update_balance(account_id, new_balance)
