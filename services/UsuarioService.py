from dtos.UsuarioSalvar import UsuarioSalvar

from decouple import config

from repositories.UsuarioRepository import UsuarioRepository

usuarioRepository = UsuarioRepository()

class UsuarioService:
	def criar_usuario(self, usuario: UsuarioSalvar):
		try:
			ja_existe = usuarioRepository.ja_existe(usuario)
			if ja_existe:
				return None
			else:
				return usuarioRepository.criar_usuario(usuario)
		except Exception as ex:
			raise(ex)

	def listar_todos(self):
		return usuarioRepository.listar_todos()

	def buscar_por_id(self, id: str):
		return usuarioRepository.buscar_por_id(id)