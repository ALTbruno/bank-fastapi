from datetime import datetime
from dtos.TransferSend import TransferSend
from models.TransferModel import TransferModel
from repositories.TransferRepository import TransferRepository
from services.AccountService import AccountService

transferRepository = TransferRepository()
accountService = AccountService()

class TransferService:

    def create(self, origin_account_id: str, transfer: TransferSend):

        transfer_value_in_cents = transfer.value_in_cents

        #TODO: Verificar se balance >= transfer_value_in_cents
        origin_account_balance = int(accountService.get_balance(origin_account_id)['balance'])
        origin_account_balance -= transfer_value_in_cents
        accountService.update_balance(origin_account_id, origin_account_balance)

        destination_account_balance = int(accountService.get_balance(transfer.destination_account_id)['balance'])
        destination_account_balance += transfer_value_in_cents
        accountService.update_balance(transfer.destination_account_id, destination_account_balance)
        

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
