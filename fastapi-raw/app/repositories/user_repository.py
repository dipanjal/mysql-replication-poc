import logging
from typing import Optional

from app.config.database import get_db_connection
from app.exceptions import UserNotFoundError
from app.schemas.user import UserCreate, UserUpdate

logger = logging.getLogger(__name__)

class UserRepository:
    """Repository for user database operations using raw SQL"""
    
    def create(self, user_data: UserCreate) -> int:
        """Create a new user"""

        with get_db_connection() as connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO users (name) VALUES (%s)"
            cursor.execute(insert_query, (user_data.name,))
            user_id = cursor.lastrowid
            connection.commit()
            return user_id

    def get_by_id(self, user_id: int) -> Optional[tuple[any]]:
        """Get user by ID"""

        with get_db_connection() as connection:
            cursor = connection.cursor()
            select_query = "SELECT id, name FROM users WHERE id = %s"
            cursor.execute(select_query, (user_id,))
            user_record = cursor.fetchone()

            if not user_record:
                raise UserNotFoundError()

            return user_record

    def get_all(self) -> tuple[tuple[any]]:
        """Get all users"""

        with get_db_connection() as connection:
            cursor = connection.cursor()
            select_query = "SELECT id, name FROM users ORDER BY id"
            cursor.execute(select_query)
            user_rows = cursor.fetchall()
            return user_rows

    def update(self, user_id: int, user_data: UserUpdate):
        """Update user by ID"""

        # First check if user exists
        self.get_by_id(user_id)

        with get_db_connection() as connection:
            cursor = connection.cursor()
            update_query = "UPDATE users SET name = %s WHERE id = %s"
            cursor.execute(update_query, (user_data.name, user_id))
            connection.commit()

    def delete(self, user_id: int):
        """Delete user by ID"""

        # First check if user exists
        self.get_by_id(user_id)

        with get_db_connection() as connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM users WHERE id = %s"
            cursor.execute(delete_query, (user_id,))
            connection.commit()
            logger.info("User deleted successfully associated with id=%s", user_id)