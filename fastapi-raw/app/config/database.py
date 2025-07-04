import os
import logging
from contextlib import contextmanager
import pymysql

logger = logging.getLogger(__name__)

# Database configuration from environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', '127.0.0.1'),
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