from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Todo CRUD"
    DATABASE_URL: str = "sqlite:///./todo.db"
    JWT_SECRET_KEY: str = "change-me-in-env"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    BOOTSTRAP_SUPERADMIN_EMAIL: str = ""
    BOOTSTRAP_SUPERADMIN_PASSWORD: str = ""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
