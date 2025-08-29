import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'

load_dotenv(dotenv_path=env_path)

class Config:
    PROJECT_TITLE: str = "Blogs"
    PROJECT_VERSION: str = "0.1.0"
    POSTGRES_USER: str =os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str =os.getenv("POSTGRES_PASSWORD", "admin")
    POSTGRES_SERVER: str =os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: int =os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str =os.getenv("POSTGRES_DB", "blogdbcourse")
    POSTGRES_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

config = Config()
