from dtos.UsuarioSalvar import UsuarioSalvar
from repositories.UsuarioRepository import UsuarioRepository
from repositories.ContaRepository import ContaRepository
from services.ContaService import ContaService

usuarioRepository = UsuarioRepository()
contaRepository = ContaRepository()
contaService = ContaService()

class UsuarioService:
	def criar_usuario(self, usuario: UsuarioSalvar):
		try:
			ja_existe = usuarioRepository.ja_existe(usuario)
			if ja_existe:
				return None
			else:
				usuario = usuarioRepository.criar_usuario(usuario)
				# * deixar assim? ou fazer via contaRepository?
				contaService.criar_conta(usuario['id'])
				return usuario
		except Exception as ex:
			raise(ex)

	def listar_todos(self):
		return usuarioRepository.listar_todos()

	def buscar_por_id(self, id: str):
		return usuarioRepository.buscar_por_id(id)