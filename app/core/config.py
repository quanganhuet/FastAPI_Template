from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Clean Template"
    debug: bool = False
    database_url: str = "mysql+pymysql://user:password@mysql:3306/fastapi_db"
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()