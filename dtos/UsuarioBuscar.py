from pydantic import BaseModel, Field, EmailStr

class UsuarioBuscar(BaseModel):
	id: str = Field(...)
	nome: str = Field(...)
	sobrenome: str = Field(...)
	cpf: str = Field(...)
	email: EmailStr = Field(...)

