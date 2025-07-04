from typing import List

from fastapi import APIRouter, status

from app.exceptions import DatabaseError
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user"""
    try:
        return UserService().create_user(user)
    except Exception as e:
        raise DatabaseError(f"Failed to create user: {str(e)}")

@router.get("/", response_model=List[UserResponse])
async def get_users():
    """Get all users"""
    return UserService().get_users()

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """Get a specific user by ID"""
    return UserService().get_user(user_id)

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate):
    """Update a user"""
    return UserService().update_user(user_id, user)

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """Delete a user"""
    UserService().delete_user(user_id)