import re
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, validator

class CustomerSave(BaseModel):
	name: str = Field(...)
	last_name: str = Field(...)
	cpf: str = Field(...)
	birth_date: str = Field(...)
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

	@validator('birth_date')
	def validate_date_format_and_age(cls, birth_date):
		if not re.match('^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$', birth_date):
			raise ValueError('Date format must be yyyy-MM-dd')
		
		today = datetime.today()
		birth = datetime.strptime(birth_date, '%Y-%m-%d')
		age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
		
		if age < 18:
			raise ValueError('You must be 18 or older to register')

		return birth_date
