from fastapi import FastAPI
from controllers.HealthController import router as HealthController
from controllers.UsuarioController import router as UsuarioController
from controllers.ContaController import router as ContaController

app = FastAPI()

app.include_router(HealthController, tags=["Health"], prefix="/api/health")
app.include_router(UsuarioController, tags=["Usuário"], prefix="/api/usuarios")
app.include_router(ContaController, tags=["Conta"], prefix="/api/contas")