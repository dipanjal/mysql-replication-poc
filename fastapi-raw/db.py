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
        return None
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
    connection = get_db_connection()
    if not connection:
        raise Exception("Database connection failed")

    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(insert_query, (name,))

        user_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()

        return user_id
    except Error as e:
        if connection:
            connection.close()
        raise Exception(f"Database error: {str(e)}")

def get_all_users_db():
    """Get all users from database"""
    connection = get_db_connection()
    if not connection:
        raise Exception("Database connection failed")

    try:
        cursor = connection.cursor(dictionary=True)
        select_query = "SELECT id, name FROM users ORDER BY id"
        cursor.execute(select_query)

        users = cursor.fetchall()
        cursor.close()
        connection.close()

        return users
    except Error as e:
        if connection:
            connection.close()
        raise Exception(f"Database error: {str(e)}")

def get_user_by_id_db(user_id):
    """Get a specific user by ID from database"""
    connection = get_db_connection()
    if not connection:
        raise Exception("Database connection failed")

    try:
        cursor = connection.cursor(dictionary=True)
        select_query = "SELECT id, name FROM users WHERE id = %s"
        cursor.execute(select_query, (user_id,))

        user = cursor.fetchone()
        cursor.close()
        connection.close()

        return user
    except Error as e:
        if connection:
            connection.close()
        raise Exception(f"Database error: {str(e)}")

def update_user_db(user_id, name):
    """Update a user in database"""
    connection = get_db_connection()
    if not connection:
        raise Exception("Database connection failed")

    try:
        cursor = connection.cursor()

        # Check if user exists
        check_query = "SELECT id FROM users WHERE id = %s"
        cursor.execute(check_query, (user_id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return False

        # Update user
        update_query = "UPDATE users SET name = %s WHERE id = %s"
        cursor.execute(update_query, (name, user_id))
        connection.commit()
        cursor.close()
        connection.close()

        return True
    except Error as e:
        if connection:
            connection.close()
        raise Exception(f"Database error: {str(e)}")

def delete_user_db(user_id):
    """Delete a user from database"""
    connection = get_db_connection()
    if not connection:
        raise Exception("Database connection failed")

    try:
        cursor = connection.cursor()

        # Check if user exists
        check_query = "SELECT id FROM users WHERE id = %s"
        cursor.execute(check_query, (user_id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return False

        # Delete user
        delete_query = "DELETE FROM users WHERE id = %s"
        cursor.execute(delete_query, (user_id,))
        connection.commit()
        cursor.close()
        connection.close()

        return True
    except Error as e:
        if connection:
            connection.close()
        raise Exception(f"Database error: {str(e)}")