from fastapi import APIRouter, HTTPException, status
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user"""
    try:
        return UserService().create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.get("/", response_model=List[UserResponse])
async def get_users():
    """Get all users"""
    try:
        return UserService().get_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """Get a specific user by ID"""
    try:
        user = UserService().get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate):
    """Update a user"""
    try:
        user_response = UserService().update_user(user_id, user)
        if not user_response:
            raise HTTPException(status_code=404, detail="User not found")
        return user_response
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """Delete a user"""
    try:
        success = UserService().delete_user(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}") 