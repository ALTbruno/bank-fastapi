from pydantic import BaseModel, Field, EmailStr

class UsuarioModel(BaseModel):
	nome: str = Field(...)
	sobrenome: str =Field(...)
	cpf: str = Field(...)
	email: EmailStr = Field(...)
	senha: str = Field(...)
