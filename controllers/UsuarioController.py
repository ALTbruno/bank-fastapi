import json
from fastapi import APIRouter

from models.UsuarioModel import UsuarioModel
import services.UsuarioService as UsuarioService
router = APIRouter()

@router.post("/", response_description="Rota para criação de um usuário")
async def criar_usuario(usuario: UsuarioModel):
	return await UsuarioService.criar_usuario(usuario)