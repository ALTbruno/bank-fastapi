from fastapi import APIRouter, Body, Response
from fastapi.responses import JSONResponse
from dtos.TransferSend import TransferSend

from exceptions.BusinessException import BusinessException
from services.AccountService import AccountService
from services.TransferService import TransferService

ROUTER = APIRouter(prefix="/api/accounts", tags=["Account"])

accountService = AccountService()
transferService = TransferService()

@ROUTER.get("", response_description="Lista todas as Contas")
def get_all():
    return accountService.get_all()

@ROUTER.get("/{id}", response_description="Retorna uma Conta")
def find_by_id(id: str):
    return accountService.find_by_id(id)

@ROUTER.get("/{id}/balance", response_description="Retorna o saldo de uma Conta")
def get_balance(id: str):
    return accountService.get_balance(id)

@ROUTER.post("/{origin_account_id}/transfer", response_description="Efetua uma Transferência")
def transfer(response: Response, origin_account_id: str, transfer: TransferSend = Body(...)):
    try:
        transfer = transferService.create(origin_account_id, transfer)
        return JSONResponse(status_code=201, content=transfer)
    except BusinessException as ex:
        response.status_code = ex.status_code
        return ex

@ROUTER.get("/{id}/transactions", response_description="Retorna transações de uma conta (enviadas e recebidas)")
def get_transactions_by_account_id(id: str, start_date: str | None = None, end_date: str | None = None):
    return transferService.get_by_account(id, start_date, end_date)
