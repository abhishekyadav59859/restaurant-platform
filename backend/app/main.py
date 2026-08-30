from fastapi import FastAPI
from app.api.auth.routes import router as auth_router

app = FastAPI(title="Restaurant Platform API")

app.include_router(auth_router)