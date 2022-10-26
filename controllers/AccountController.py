from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from dtos.TransferSend import TransferSend

from services.AccountService import AccountService
from services.TransferService import TransferService

router = APIRouter()

accountService = AccountService()
transferService = TransferService()

@router.get("/", response_description="Lista todas as Contas")
def get_all():
    return accountService.get_all()

@router.get("/{id}", response_description="Retorna uma Conta")
def find_by_id(id: str):
    return accountService.find_by_id(id)

@router.get("/{id}/balance", response_description="Retorna o saldo de uma Conta")
def get_balance(id: str):
    return accountService.get_balance(id)

@router.post("/{origin_account_id}/transfer", response_description="Efetua uma Transferência")
def transfer(origin_account_id: str, transfer: TransferSend = Body(...)):
    transfer = transferService.create(origin_account_id, transfer)
    return JSONResponse(status_code=201, content=transfer)

@router.get("/{id}/transactions", response_description="Retorna transações de uma conta (enviadas e recebidas)")
def get_transactions_by_account_id(id: str):
    return transferService.get_by_account(id)
