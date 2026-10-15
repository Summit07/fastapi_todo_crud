from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from src.config.settings import settings
from src.config.database import Base, engine, SessionLocal
from src.routers.api import api_router
from src.services.auth_service import bootstrap_superadmin


bearer_scheme = HTTPBearer()

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        bootstrap_superadmin(db)
    finally:
        db.close()
    yield

app = FastAPI(title=settings.APP_NAME, version="1.0.0", lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
