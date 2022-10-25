from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from dtos.CustomerSave import CustomerSave
from services.CustomerService import CustomerService

router = APIRouter()

customerService = CustomerService()

@router.post("/", response_description="Rota para criação de um usuário")
def create(customer: CustomerSave = Body(...)):
	try:
		customer = customerService.create(customer)
		if customer is None:
			return JSONResponse(status_code=400, content={'message': 'Usuário já cadastrado'})
		return JSONResponse(status_code=201, content=customer)
	except Exception as ex:
		raise ex


@router.get("/", response_description="Rota para listagem de todos os usuários")
def get_all():
	return customerService.get_all()

@router.get("/{id}", response_description="Retorna um único usuário")
def find_by_id(id: str):
	return customerService.find_by_id(id)