from pydantic import BaseModel, Field, EmailStr

class CustomerFind(BaseModel):
	id: str = Field(...)
	name: str = Field(...)
	last_name: str = Field(...)
	cpf: str = Field(...)
	email: EmailStr = Field(...)

