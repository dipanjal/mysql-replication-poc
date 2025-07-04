from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from contextlib import asynccontextmanager
from db import (
    check_db_connection, 
    init_database, 
    create_user_db, 
    get_all_users_db, 
    get_user_by_id_db, 
    update_user_db, 
    delete_user_db
)

# Pydantic models
class UserCreate(BaseModel):
    name: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    name: Optional[str] = None

class HealthStatus(BaseModel):
    application: str
    database: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up...")
    init_database()
    yield
    # Shutdown
    print("Shutting down...")

# FastAPI app
app = FastAPI(
    title="User Management API",
    description="A simple FastAPI application with MySQL using raw SQL queries",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/healthz", response_model=HealthStatus)
async def health_check():
    """Health check endpoint"""
    # Check application status
    app_status = "running"
    
    # Check database status
    db_status = "running" if check_db_connection() else "not running"
    
    return HealthStatus(application=app_status, database=db_status)

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user"""
    try:
        user_id = create_user_db(user.name)
        return UserResponse(id=user_id, name=user.name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/users", response_model=List[UserResponse])
async def get_users():
    """Get all users"""
    try:
        users = get_all_users_db()
        return [UserResponse(**user) for user in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """Get a specific user by ID"""
    try:
        user = get_user_by_id_db(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(**user)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate):
    """Update a user"""
    try:
        success = update_user_db(user_id, user.name)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(id=user_id, name=user.name)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete a user"""
    try:
        success = delete_user_db(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)