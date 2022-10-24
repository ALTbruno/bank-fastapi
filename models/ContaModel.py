from pydantic import BaseModel, Field

class ContaModel(BaseModel):
	agencia: str = Field(...)
	numero: str = Field(...)
	saldo: int = Field(...)
	cliente_id: str = Field(...)
