from fastapi import APIRouter

router = APIRouter()

@router.get("/", response_description="Rota que verifica se a API está ON")
def health():
	return "De boa na lagoa"