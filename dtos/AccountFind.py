from pydantic import BaseModel, Field

class AccountModel(BaseModel):
    id: str = Field(...)
    agency_number: str = Field(...)
    account_number: str = Field(...)
    balance: int = Field(...)
    customer_id: str = Field(...)
