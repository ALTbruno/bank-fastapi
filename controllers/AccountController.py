from fastapi import APIRouter, Body
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
    return transferService.create(origin_account_id, transfer)
