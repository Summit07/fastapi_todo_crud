from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.config.constants import Role
from src.config.settings import settings
from src.models.user import User
from src.schemas.auth_schema import UserRegisterSchema, UserLoginSchema, UserSchema
from src.utils.security import hash_password, verify_password, create_access_token

def register_user(db: Session, data: UserRegisterSchema) -> UserSchema:
    existing = db.scalar(select(User).where(User.email == data.email))
    if existing:
        raise HTTPException(status_code=409, detail="Email is already registered")
    user = User(email=str(data.email).lower(), hashed_password=hash_password(data.password), role=Role.USER.value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserSchema.model_validate(user)

def authenticate_user(db: Session, data: UserLoginSchema) -> str:
    user = db.scalar(select(User).where(User.email == str(data.email).lower()))
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    return create_access_token(subject=str(user.id), role=user.role)

def bootstrap_superadmin(db: Session) -> None:
    email = settings.BOOTSTRAP_SUPERADMIN_EMAIL.strip().lower()
    password = settings.BOOTSTRAP_SUPERADMIN_PASSWORD
    if not email or not password:
        return
    existing = db.scalar(select(User).where(User.email == email))
    if existing:
        return
    user = User(email=email, hashed_password=hash_password(password), role=Role.SUPERADMIN.value)
    db.add(user)
    db.commit()
