from datetime import date
from datetime import datetime
from pydantic import Field

class TransferModel:
    origin_account_id: str = Field(...)
    destination_account_id: str = Field(...)
    value_in_cents: int = Field(...)
    datetime: datetime = Field(...)
