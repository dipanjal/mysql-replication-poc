from fastapi import HTTPException, status


class DatabaseError(HTTPException):
    """Custom exception for database-related errors"""
    def __init__(self, detail: str = "Database error occurred"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)


class UserNotFoundError(HTTPException):
    """Custom exception for when a user is not found"""
    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class ValidationError(HTTPException):
    """Custom exception for validation errors"""
    def __init__(self, detail: str = "Validation error"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
