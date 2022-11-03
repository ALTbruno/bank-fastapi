from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

from exceptions.BusinessException import BusinessException
from dtos.TransferSend import TransferSend
from models.TransferModel import TransferModel
from repositories.TransferRepository import TransferRepository
from services.AccountService import AccountService

transferRepository = TransferRepository()
accountService = AccountService()

class TransferService:

    def create(self, origin_account_id: str, transfer: TransferSend):

        destination_account_id = transfer.destination_account_id

        if origin_account_id == destination_account_id:
            raise BusinessException (400, "destination_account_id must be different from origin_account_id")

        transfer_value_in_cents = transfer.value_in_cents

        origin_account_balance = int(accountService.get_balance(origin_account_id)['balance'])
        if origin_account_balance < transfer_value_in_cents:
            raise BusinessException(400, "Insufficient balance")
        origin_account_balance -= transfer_value_in_cents
        accountService.update_balance(origin_account_id, origin_account_balance)

        destination_account_balance = int(accountService.get_balance(destination_account_id)['balance'])
        destination_account_balance += transfer_value_in_cents
        accountService.update_balance(destination_account_id, destination_account_balance)

        transfer_model = self.convert_send_to_model(origin_account_id, transfer)
        transfer_repository = transferRepository.create(transfer_model)
        return self.convert_to_transfer_find(transfer_repository)

    def convert_send_to_model(self, origin_account_id: str, transfer: TransferSend):
        transfer_model = TransferModel()
        transfer_model.origin_account_id = origin_account_id
        transfer_model.destination_account_id = transfer.destination_account_id
        transfer_model.value_in_cents = transfer.value_in_cents
        transfer_model.datetime = datetime.now()
        return transfer_model

    def convert_to_transfer_find(self, transfer):
        return {
            'id': str(transfer['_id']),
            'origin_account_id': str(transfer['origin_account_id']),
            'destination_account_id': str(transfer['destination_account_id']),
            'value_in_cents': str(transfer['value_in_cents']),
            'datetime': str(transfer['datetime'])
        }

    def get_by_account(self, account_id: str, start_date: str | None = None, end_date: str | None = None):

        transfers = []

        if start_date and end_date:
            start_date = parse(start_date)
            end_date = parse(end_date)
            end_date += relativedelta(day=end_date.day+1)

            for transfer in transferRepository.get_by_account_and_dates(account_id, start_date, end_date):
                transfers.append(self.convert_to_transfer_find(transfer))
        else:
            for transfer in transferRepository.get_by_account(account_id):
                transfers.append(self.convert_to_transfer_find(transfer))

        return transfers
