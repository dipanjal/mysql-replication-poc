from typing import List, Optional

from app.helper import Mapper
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate, UserResponse


class UserService:
    """Service layer for user business logic"""
    
    def __init__(self):
        self.repository = UserRepository()
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        """Create a new user"""
        user_id = self.repository.create(user_data)
        return UserResponse(**user_data.model_dump(), id=user_id)

    def get_user(self, user_id: int) -> Optional[UserResponse]:
        """Get user by ID"""
        return Mapper.to_schema(
            row=self.repository.get_by_id(user_id),
            schema=UserResponse
        )

    def get_users(self) -> List[UserResponse]:
        """Get all users"""
        return Mapper.to_schemas(
            rows=self.repository.get_all(),
            schema=UserResponse
        )
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
        """Update user by ID"""
        updated = self.repository.update(user_id, user_data)
        if updated:
            return UserResponse(**user_data.model_dump(), id=user_id)
        return None
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user by ID"""
        return self.repository.delete(user_id) 