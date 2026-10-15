from fastapi import APIRouter
from src.routers.auth_router import router as auth_router
from src.routers.todo_router import router as todo_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(todo_router)
