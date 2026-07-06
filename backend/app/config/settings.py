from pydantic import BaseSettings, Field, AnyUrl
from typing import List


class Settings(BaseSettings):
    APP_HOST: str = Field("0.0.0.0")
    APP_PORT: int = Field(8000)

    DATABASE_HOST: str = Field("127.0.0.1")
    DATABASE_PORT: int = Field(3306)
    DATABASE_USER: str = Field("gsz_user")
    DATABASE_PASSWORD: str = Field("change_me")
    DATABASE_NAME: str = Field("global_smart_zone")

    SECRET_KEY: str = Field(...)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60)
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(7)

    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    SMTP_HOST: str = Field(None)
    SMTP_PORT: int = Field(587)
    SMTP_USER: str = Field(None)
    SMTP_PASSWORD: str = Field(None)

    TWILIO_ACCOUNT_SID: str = Field(None)
    TWILIO_AUTH_TOKEN: str = Field(None)
    TWILIO_WHATSAPP_FROM: str = Field(None)

    UPLOAD_PATH: str = Field("uploads")
    RATE_LIMIT_PER_MINUTE: int = Field(120)

    class Config:
        env_file = ".env"


settings = Settings()
