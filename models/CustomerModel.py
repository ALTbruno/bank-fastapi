from pydantic import BaseModel, Field, EmailStr

class CustomerModel(BaseModel):
	name: str = Field(...)
	last_name: str = Field(...)
	cpf: str = Field(...)
	birth_date: str = Field(...)
	email: EmailStr = Field(...)
	password: str = Field(...)
