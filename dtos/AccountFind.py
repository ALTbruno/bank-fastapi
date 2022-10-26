from pydantic import BaseModel, Field

class AccountFind(BaseModel):
    id: str = Field(...)
    agency_number: str = Field(...)
    account_number: str = Field(...)
    balance: int = Field(...)
    customer_id: str = Field(...)
