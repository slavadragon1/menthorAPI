# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///../test.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL,
                             echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
