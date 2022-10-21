import motor.motor_asyncio

from decouple import config
from bson import ObjectId
from dtos.UsuarioBuscar import UsuarioBuscar
from dtos.UsuarioSalvar import UsuarioSalvar

MONGODB_URL = config("MONGODB_URL")

mongodb = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = mongodb.bank_fastapi

usuario_collection = database.get_collection("usuarios")

def converter_para_UsuarioBuscar(usuario):
	return {
		"id": str(usuario["_id"]),
		"nome":  str(usuario["nome"]),
		"sobrenome": str(usuario["sobrenome"]),
		"cpf": str(usuario["cpf"]),
		"email": str(usuario["email"])
	}

async def criar_usuario(usuario: UsuarioSalvar) -> UsuarioBuscar:
	usuario_dict = await usuario_collection.insert_one(usuario.__dict__)
	usuario_criado = await usuario_collection.find_one({ "_id": usuario_dict.inserted_id })
	return converter_para_UsuarioBuscar(usuario_criado)

# NAO TA FUNCIONANDO
async def listar_todos():
	# tipo: AsyncIOMotorCursor
	return usuario_collection.find()

async def buscar_por_id(id: str) -> dict:
	usuario = await usuario_collection.find_one({ "_id": ObjectId(id) })
	if usuario:
		return converter_para_UsuarioBuscar(usuario)

