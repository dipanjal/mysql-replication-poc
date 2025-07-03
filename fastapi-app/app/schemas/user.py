from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    """Schema for creating a new user"""
    name: str

class UserUpdate(BaseModel):
    """Schema for updating a user"""
    name: Optional[str] = None

class UserResponse(BaseModel):
    """Schema for user response"""
    id: int
    name: Optional[str] = None

    class Config:
        from_attributes = True  # SQLAlchemy → Pydantic conversion
