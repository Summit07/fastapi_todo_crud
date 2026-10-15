from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.config.database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(30), default="users", nullable=False)
    todos: Mapped[list["Todo"]] = relationship(back_populates="owner", cascade="all, delete-orphan")