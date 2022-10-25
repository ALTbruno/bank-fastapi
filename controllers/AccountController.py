from fastapi import APIRouter

from services.AccountService import AccountService

router = APIRouter()

accountService = AccountService()

@router.get("/", response_description="Lista todas as Contas")
def get_all():
    return accountService.get_all()
