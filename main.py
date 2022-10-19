from fastapi import FastAPI
from controllers.HealthController import router as HealthController

app = FastAPI()

app.include_router(HealthController, tags=["Health"], prefix="/api/health")
