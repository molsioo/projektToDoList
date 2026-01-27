from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv()

engine = create_engine(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/todo",
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
