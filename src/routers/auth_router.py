from fastapi import APIRouter, status
from src.middleware.auth_middleware import CurrentUser, DbSession
from src.controllers import auth_controller
from src.dto.auth_dto import RegisterRequestDTO, LoginRequestDTO, TokenResponseDTO, UserResponseDTO

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequestDTO, db: DbSession):
    return auth_controller.register(db, data)

@router.post("/login", response_model=TokenResponseDTO)
def login(data: LoginRequestDTO, db: DbSession):
    return auth_controller.login(db, data)

@router.get("/me", response_model=UserResponseDTO)
def me(user: CurrentUser):
    return auth_controller.me(user)
