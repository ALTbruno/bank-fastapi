from datetime import date
from pydantic import BaseModel, Field

class TransferSend(BaseModel):
    destination_account_id: str = Field(...)
    value_in_cents: int = Field(...)
