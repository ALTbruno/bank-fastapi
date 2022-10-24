from random import randrange
from models.ContaModel import ContaModel

from repositories.ContaRepository import ContaRepository

contaRepository = ContaRepository()

class ContaService:
	
	def gerar_numero(self):
		return str(randrange(1000000000, 9000000000))

	def criar_conta(self, cliente_id: str):
		numero_conta = self.gerar_numero()
		while contaRepository.conta_ja_existe(numero_conta):
			numero_conta = self.gerar_numero()
		conta = ContaModel(agencia = '0001', numero = numero_conta, saldo = 0, cliente_id = cliente_id)
		return contaRepository.criar_conta(conta)
