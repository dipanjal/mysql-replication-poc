import os
import logging
from contextlib import contextmanager

import pymysql

logger = logging.getLogger(__name__)

# Database configuration from environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', '103.174.50.21'),
    'port': int(os.getenv('DB_PORT', 6033)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'sbtest'),
    'charset': 'utf8mb4',
    'autocommit': True
}

@contextmanager
def get_db_connection():
    """Get database connection"""
    connection = None
    try:
        connection = pymysql.connect(**DB_CONFIG)
        yield connection
    except Exception as e:
        logger.exception(e)
        raise e
    finally:
        if connection:
            connection.close()

def check_db_connection():
    """Check if database connection is working"""
    with get_db_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            return True
        except Exception as e:
            logger.exception(e)
            return False

def create_user_db(name):
    """Create a new user in database"""
    with get_db_connection() as connection:
        try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO users (name) VALUES (%s)"
            cursor.execute(insert_query, (name,))

            user_id = cursor.lastrowid
            connection.commit()
            return user_id
        except Exception as e:
            logger.exception(e)
            raise RuntimeError(f"Database error: {str(e)}")

def get_all_users_db():
    """Get all users from database"""
    with get_db_connection() as connection:
        try:
            cursor = connection.cursor(dictionary=True)
            select_query = "SELECT id, name FROM users ORDER BY id"
            cursor.execute(select_query)
            users = cursor.fetchall()
            return users
        except Exception as e:
            logger.exception(e)
            raise Exception(f"Database error: {str(e)}")

def get_user_by_id_db(user_id):
    """Get a specific user by ID from database"""
    with get_db_connection() as connection:
        try:
            cursor = connection.cursor(dictionary=True)
            select_query = "SELECT id, name FROM users WHERE id = %s"
            cursor.execute(select_query, (user_id,))
            user = cursor.fetchone()
            return user
        except Exception as e:
            logger.exception(e)
            raise Exception(f"Database error: {str(e)}")

def update_user_db(user_id, name):
    """Update a user in database"""

    existed_user = get_user_by_id_db(user_id)
    if not existed_user:
        raise RuntimeError(f"User associated with id={user_id} Not found")

    with get_db_connection() as connection:
        try:
            cursor = connection.cursor()

            # Update user
            update_query = "UPDATE users SET name = %s WHERE id = %s"
            cursor.execute(update_query, (name, user_id))
            connection.commit()
            return True
        except Exception as e:
            logger.exception(e)
            raise Exception(f"Database error: {str(e)}")

def delete_user_db(user_id):
    """Delete a user from database"""

    existed_user = get_user_by_id_db(user_id)
    if not existed_user:
        raise RuntimeError(f"User associated with id={user_id} Not found")

    with get_db_connection() as connection:
        try:
            cursor = connection.cursor()
            # Delete user
            delete_query = "DELETE FROM users WHERE id = %s"
            cursor.execute(delete_query, (user_id,))
            connection.commit()
            logger.info("User Deleted successfully associated with id=%s", user_id)
            return True
        except Exception as e:
            logger.exception(e)
            raise Exception(f"Database error: {str(e)}")