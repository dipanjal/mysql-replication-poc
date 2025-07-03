from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from typing import List, Optional

class UserService:
    """Service layer for user business logic"""
    
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        """Create a new user"""
        user = self.repository.create(user_data)
        return UserResponse.from_orm(user)
    
    def get_user(self, user_id: int) -> Optional[UserResponse]:
        """Get user by ID"""
        user = self.repository.get_by_id(user_id)
        if user:
            return UserResponse.from_orm(user)
        return None
    
    def get_users(self, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        """Get all users with pagination"""
        users = self.repository.get_all(skip, limit)
        return [UserResponse.from_orm(user) for user in users]
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
        """Update user by ID"""
        user = self.repository.update(user_id, user_data)
        if user:
            return UserResponse.from_orm(user)
        return None
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user by ID"""
        return self.repository.delete(user_id) 