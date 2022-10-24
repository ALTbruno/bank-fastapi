from decouple import config
from pymongo import MongoClient
from bson import ObjectId
from dtos.UsuarioSalvar import UsuarioSalvar

MONGODB_URL = config("MONGODB_URL")

mongo_client = MongoClient(MONGODB_URL)
database = mongo_client.bank_fastapi
usuarios_collection = database.usuarios

class UsuarioRepository:

	def converter_para_UsuarioBuscar(self, usuario):
		return {
			"id": str(usuario['_id']),
			'nome':  str(usuario['nome']),
			'sobrenome': str(usuario['sobrenome']),
			'cpf': str(usuario['cpf']),
			'email': str(usuario['email'])
		}

	def criar_usuario(self, usuario: UsuarioSalvar):
		usuario_id = usuarios_collection.insert_one(usuario.__dict__).inserted_id
		usuario_criado = usuarios_collection.find_one({ '_id': usuario_id })
		return self.converter_para_UsuarioBuscar(usuario_criado)

	def listar_todos(self):
		usuarios = []
		for usuario in usuarios_collection.find():
			usuarios.append(self.converter_para_UsuarioBuscar(usuario))

		return usuarios

	def buscar_por_id(self, id: str):
		usuario = usuarios_collection.find_one({ '_id': ObjectId(id) })
		return self.converter_para_UsuarioBuscar(usuario)

	def ja_existe(self, usuario: UsuarioSalvar) -> bool:
		existe_usuario_cpf = usuarios_collection.count_documents({'cpf': usuario.cpf}) > 0
		existe_usuario_email = usuarios_collection.count_documents({'email': usuario.email}) > 0
		return existe_usuario_cpf or existe_usuario_email