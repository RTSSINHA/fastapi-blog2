from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import config

SQLALCHEMY_DATABASE_URL = config.POSTGRES_URL

print("Database URL: "+SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)

