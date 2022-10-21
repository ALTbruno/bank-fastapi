from dtos.UsuarioSalvar import UsuarioSalvar
import repositories.UsuarioRepository as UsuarioRepository

async def criar_usuario(usuario: UsuarioSalvar):
	return await UsuarioRepository.criar_usuario(usuario)

async def listar_todos():
	return await UsuarioRepository.listar_todos()

async def buscar_por_id(id: str):
	return await UsuarioRepository.buscar_por_id(id)