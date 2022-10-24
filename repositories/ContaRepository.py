from decouple import config
from pymongo import MongoClient
from bson import ObjectId

from models.ContaModel import ContaModel

MONGODB_URL = config("MONGODB_URL")

mongo_client = MongoClient(MONGODB_URL)
database = mongo_client.bank_fastapi
contas_collection = database.contas

class ContaRepository:
	
	def criar_conta(self, conta: ContaModel):
		conta_id = contas_collection.insert_one(conta.__dict__).inserted_id
		conta_criada = contas_collection.find_one({ '_id': ObjectId(conta_id)})
		return conta_criada

	def listar_todas(self):
		contas = []
		for conta in contas_collection.find():
			contas.append(self.converter(conta))
		return contas

	def converter(self, conta):
		return {
			'id': str(conta['_id']),
			'agencia': str(conta['agencia']),
			'numero': str(conta['numero']),
			'saldo': str(conta['saldo']),
			'cliente_id': str(conta['cliente_id'])
		}
	def conta_ja_existe(self, numero: str) -> bool:
		return contas_collection.count_documents({'numero': numero}) > 0
