from sqlalchemy.orm import Session
from src.dto.auth_dto import RegisterRequestDTO, LoginRequestDTO, TokenResponseDTO, UserResponseDTO
from src.models.user import User
from src.schemas.auth_schema import UserRegisterSchema, UserLoginSchema
from src.services import auth_service

def register(db: Session, data: RegisterRequestDTO) -> UserResponseDTO:
    schema = UserRegisterSchema(email=data.email, password=data.password)
    user_schema = auth_service.register_user(db, schema)
    return UserResponseDTO.model_validate(user_schema)

def login(db: Session, data: LoginRequestDTO) -> TokenResponseDTO:
    schema = UserLoginSchema(email=data.email, password=data.password)
    token = auth_service.authenticate_user(db, schema)
    return TokenResponseDTO(access_token=token, token_type="bearer")

def me(user: User) -> UserResponseDTO:
    return UserResponseDTO.model_validate(user)
