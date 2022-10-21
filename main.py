from fastapi import FastAPI
from controllers.HealthController import router as HealthController
from controllers.UsuarioController import router as UsuarioController

app = FastAPI()

app.include_router(HealthController, tags=["Health"], prefix="/api/health")
app.include_router(UsuarioController, tags=["Usuário"], prefix="/api/usuarios")