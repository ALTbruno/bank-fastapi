from models.UsuarioModel import UsuarioModel
import repositories.UsuarioRepository as UsuarioRepository

async def criar_usuario(usuario: UsuarioModel):
	return await UsuarioRepository.criar_usuario(usuario)