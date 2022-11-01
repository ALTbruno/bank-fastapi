from fastapi import APIRouter

ROUTER = APIRouter(prefix="/api/health", tags=["Health"])

@ROUTER.get("/", response_description="Rota que verifica se a API está ON")
def health():
	return "De boa na lagoa"
