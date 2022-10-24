from fastapi import APIRouter, Body, HTTPException
from fastapi.responses import JSONResponse
from dtos.UsuarioSalvar import UsuarioSalvar
from services.UsuarioService import UsuarioService

router = APIRouter()

usuarioService = UsuarioService()

@router.post("/", response_description="Rota para criação de um usuário")
def criar_usuario(usuario: UsuarioSalvar = Body(...)):
	try:
		usuario = usuarioService.criar_usuario(usuario)
		if usuario is None:
			return JSONResponse(status_code=400, content={'message': 'Usuário já cadastrado'})
		return JSONResponse(status_code=201, content=usuario)
	except Exception as ex:
		raise ex


@router.get("/", response_description="Rota para listagem de todos os usuários")
def listar_todos():
	return usuarioService.listar_todos()

@router.get("/{id}", response_description="Retorna um único usuário")
def buscar_por_id(id: str):
	return usuarioService.buscar_por_id(id)