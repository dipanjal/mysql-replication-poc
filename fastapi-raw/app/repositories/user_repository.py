import logging
from typing import List, Optional, Dict, Any
from app.config.database import get_db_connection
from app.schemas.user import UserCreate, UserUpdate
from app.helper import Parser

logger = logging.getLogger(__name__)

class UserRepository:
    """Repository for user database operations using raw SQL"""
    
    def create(self, user_data: UserCreate) -> int:
        """Create a new user"""
        with get_db_connection() as connection:
            try:
                cursor = connection.cursor()
                insert_query = "INSERT INTO users (name) VALUES (%s)"
                cursor.execute(insert_query, (user_data.name,))
                user_id = cursor.lastrowid
                connection.commit()
                return user_id
            except Exception as e:
                logger.exception(e)
                raise RuntimeError(f"Database error: {str(e)}")

    def get_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get user by ID"""
        with get_db_connection() as connection:
            try:
                cursor = connection.cursor()
                select_query = "SELECT id, name FROM users WHERE id = %s"
                cursor.execute(select_query, (user_id,))
                row = cursor.fetchone()

                if not row:
                    return None

                return Parser.to_dict(row, field_sequence=["id", "name"])
            except Exception as e:
                logger.exception(e)
                raise Exception(f"Database error: {str(e)}")

    def get_all(self) -> List[Dict[str, Any]]:
        """Get all users"""
        with get_db_connection() as connection:
            try:
                cursor = connection.cursor()
                select_query = "SELECT id, name FROM users ORDER BY id"
                cursor.execute(select_query)
                users = Parser.to_dicts(
                    rows=cursor.fetchall(),
                    field_sequence=["id", "name"]
                )
                return users
            except Exception as e:
                logger.exception(e)
                raise Exception(f"Database error: {str(e)}")

    def update(self, user_id: int, user_data: UserUpdate) -> Optional[Dict[str, Any]]:
        """Update user by ID"""
        # First check if user exists
        existing_user = self.get_by_id(user_id)
        if not existing_user:
            return None

        with get_db_connection() as connection:
            try:
                cursor = connection.cursor()
                update_query = "UPDATE users SET name = %s WHERE id = %s"
                cursor.execute(update_query, (user_data.name, user_id))
                connection.commit()
                
                # Return updated user
                return self.get_by_id(user_id)
            except Exception as e:
                logger.exception(e)
                raise Exception(f"Database error: {str(e)}")

    def delete(self, user_id: int) -> bool:
        """Delete user by ID"""
        # First check if user exists
        existing_user = self.get_by_id(user_id)
        if not existing_user:
            return False

        with get_db_connection() as connection:
            try:
                cursor = connection.cursor()
                delete_query = "DELETE FROM users WHERE id = %s"
                cursor.execute(delete_query, (user_id,))
                connection.commit()
                logger.info("User deleted successfully associated with id=%s", user_id)
                return True
            except Exception as e:
                logger.exception(e)
                raise Exception(f"Database error: {str(e)}") 