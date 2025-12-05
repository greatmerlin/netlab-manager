from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "NetLab Manager"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-16",
        extra="ignore",
        case_sensitive=False,
    )

settings = Settings()