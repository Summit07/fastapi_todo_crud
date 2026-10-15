from pydantic import BaseModel, EmailStr, ConfigDict
from src.config.constants import Role

class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class UserCreateSchema(BaseModel):
    email: EmailStr
    hashed_password: str
    role: str = Role.USER.value

class UserSchema(BaseModel):
    id: int
    email: EmailStr
    role: Role
    model_config = ConfigDict(from_attributes=True)

class UserInDBSchema(UserSchema):
    hashed_password: str
