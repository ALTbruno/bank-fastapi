from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from dtos.UsuarioSalvar import UsuarioSalvar

import services.UsuarioService as UsuarioService

router = APIRouter()

@router.post("/", response_description="Rota para criação de um usuário")
async def criar_usuario(usuario: UsuarioSalvar = Body(...)):
	usuario = await UsuarioService.criar_usuario(usuario)
	return JSONResponse(status_code=201, content=usuario)

@router.get("/", response_description="Rota para listagem de todos os usuários")
async def listar_todos():
	return await UsuarioService.listar_todos()

@router.get("/{id}", response_description="Retorna um único usuário")
async def buscar_por_id(id: str):
	return await UsuarioService.buscar_por_id(id)