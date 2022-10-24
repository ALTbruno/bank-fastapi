from fastapi import APIRouter

from services.ContaService import ContaService

router = APIRouter()

contaService = ContaService()

@router.get("/", response_description="Lista todas as Contas")
def listar_todas():
    return contaService.listar_todas()
