from fastapi import APIRouter

from services.AccountService import AccountService

router = APIRouter()

accountService = AccountService()

@router.get("/", response_description="Lista todas as Contas")
def get_all():
    return accountService.get_all()

@router.get("/{id}", response_description="Retorna uma Conta")
def find_by_id(id: str):
    return accountService.find_by_id(id)

@router.get("/{id}/balance", response_description="Retorna o saldo de uma Conta")
def get_balance(id: str):
    return accountService.get_balance(id)
