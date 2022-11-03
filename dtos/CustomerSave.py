import re
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, validator

class CustomerSave(BaseModel):
	name: str = Field(...)
	last_name: str = Field(...)
	cpf: str = Field(...)
	email: EmailStr = Field(...)
	password: str = Field(...)

	@validator('name')
	def validate_name_length(cls, name):
		if len(name) < 3:
			raise ValueError('Must contain at least 3 characters')
		return name

	@validator('last_name')
	def validate_last_name_length(cls, last_name):
		if len(last_name) < 3:
			raise ValueError('Must contain at least 3 characters')
		return last_name
	
	@validator('cpf')
	def validate_cpf(cls, cpf):
		if not re.match('^([\s\d]+)$', cpf):
			raise ValueError('Must be numeric')
		if len(cpf) != 11:
			raise ValueError('Must be 11 characters long')
		return cpf
