from typing import List, Optional
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate, UserResponse

class UserService:
    """Service layer for user business logic"""
    
    def __init__(self):
        self.repository = UserRepository()
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        """Create a new user"""
        user_id = self.repository.create(user_data)
        return UserResponse(id=user_id, name=user_data.name)

    def get_user(self, user_id: int) -> Optional[UserResponse]:
        """Get user by ID"""
        user = self.repository.get_by_id(user_id)
        if user:
            return UserResponse(**user)
        return None
    
    def get_users(self) -> List[UserResponse]:
        """Get all users"""
        users = self.repository.get_all()
        return [UserResponse(**user) for user in users]
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
        """Update user by ID"""
        user = self.repository.update(user_id, user_data)
        if user:
            return UserResponse(**user)
        return None
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user by ID"""
        return self.repository.delete(user_id) 