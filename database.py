from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class APIData(Base):
    __tablename__ = 'api_data'
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Text, nullable=False)

Base.metadata.create_all(bind=engine)
