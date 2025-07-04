import logging
from typing import Optional

from app.config.database import get_db_connection
from app.schemas.user import UserCreate, UserUpdate

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

    def get_by_id(self, user_id: int) -> Optional[tuple[any]]:
        """Get user by ID"""
        with get_db_connection() as connection:
            try:
                cursor = connection.cursor()
                select_query = "SELECT id, name FROM users WHERE id = %s"
                cursor.execute(select_query, (user_id,))
                user_record = cursor.fetchone()
                return user_record
            except Exception as e:
                logger.exception(e)
                raise Exception(f"Database error: {str(e)}")

    def get_all(self) -> tuple[tuple[any]]:
        """Get all users"""
        with get_db_connection() as connection:
            try:
                cursor = connection.cursor()
                select_query = "SELECT id, name FROM users ORDER BY id"
                cursor.execute(select_query)
                user_rows = cursor.fetchall()
                return user_rows
            except Exception as e:
                logger.exception(e)
                raise Exception(f"Database error: {str(e)}")

    def update(self, user_id: int, user_data: UserUpdate) -> bool:
        """Update user by ID"""
        # First check if user exists
        existing_user = self.get_by_id(user_id)
        if not existing_user:
            return False

        with get_db_connection() as connection:
            try:
                cursor = connection.cursor()
                update_query = "UPDATE users SET name = %s WHERE id = %s"
                cursor.execute(update_query, (user_data.name, user_id))
                connection.commit()
                return True
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