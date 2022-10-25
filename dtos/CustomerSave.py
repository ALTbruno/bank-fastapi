from pydantic import BaseModel, Field, EmailStr

class CustomerSave(BaseModel):
	name: str = Field(...)
	last_name: str = Field(...)
	cpf: str = Field(...)
	email: EmailStr = Field(...)
	password: str = Field(...)
