from fastapi import FastAPI
from controllers.HealthController import router as HealthController
from controllers.CustomerController import router as CustomerController
from controllers.AccountController import router as AccountController

app = FastAPI()

app.include_router(HealthController, tags=["Health"], prefix="/api/health")
app.include_router(CustomerController, tags=["Customer"], prefix="/api/customers")
app.include_router(AccountController, tags=["Account"], prefix="/api/accounts")