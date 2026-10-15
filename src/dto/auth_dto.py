from pydantic import BaseModel, EmailStr, Field, ConfigDict
from src.config.constants import Role

class RegisterRequestDTO(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class LoginRequestDTO(BaseModel):
    email: EmailStr
    password: str

class TokenResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponseDTO(BaseModel):
    id: int
    email: EmailStr
    role: Role
    model_config = ConfigDict(from_attributes=True)

# Aliases for backward compatibility
RegisterRequest = RegisterRequestDTO
LoginRequest = LoginRequestDTO
TokenResponse = TokenResponseDTO
UserResponse = UserResponseDTO

