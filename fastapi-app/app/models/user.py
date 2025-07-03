from sqlalchemy import Column, Integer, String
from app.config.database import Base

class User(Base):
    """SQLAlchemy model for the users table"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=True) 