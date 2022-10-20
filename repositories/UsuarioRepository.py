from multiprocessing.connection import wait
import motor.motor_asyncio

from decouple import config

from models.UsuarioModel import UsuarioModel


MONGODB_URL = config("MONGODB_URL")

cliente = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = cliente.bank_fastapi

usuario_collection = database.get_collection("usuarios")

async def criar_usuario(usuario: UsuarioModel) -> dict:
	usuario_dict = await usuario_collection.insert_one(usuario.__dict__)
	usuario_criado = await usuario_collection.find_one({ "_id": usuario_dict.inserted_id })
	return {
		"nome": usuario_criado['nome'],
		"sobrenome": usuario_criado['sobrenome'],
		"cpf": usuario_criado['cpf'],
		"email": usuario_criado['email'],
	}
