from fastapi import FastAPI
from app.api.v1.router import router as api_router
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Usuarios", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")




