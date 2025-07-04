from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    """Schema for creating a new user"""
    name: Optional[str] = None

class UserUpdate(BaseModel):
    """Schema for updating a user"""
    name: Optional[str] = None

class UserResponse(BaseModel):
    """Schema for user response"""
    id: int
    name: Optional[str] = None

class HealthStatus(BaseModel):
    """Schema for health check response"""
    application: str
    database: str