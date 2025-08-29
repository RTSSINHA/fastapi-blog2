from typing import Any
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import as_declarative

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


