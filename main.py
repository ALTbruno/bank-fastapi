from fastapi import FastAPI
from controllers.HealthController import ROUTER as HealthController
from controllers.CustomerController import ROUTER as CustomerController
from controllers.AccountController import ROUTER as AccountController

app = FastAPI()

app.include_router(HealthController)
app.include_router(CustomerController)
app.include_router(AccountController)
