from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from datetime import datetime
import os
from typing import List, Optional
import logging

# ────────────────────────────────────────────────────────────────────────────────
# Logging
# ────────────────────────────────────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ────────────────────────────────────────────────────────────────────────────────
# Database
# ────────────────────────────────────────────────────────────────────────────────
DATABASE_URL = os.getenv("DATABASE_URL") or "mysql+pymysql://root:password@103.174.50.21:6033/sbtest"
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set")

engine        = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal  = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base          = declarative_base()

class User(Base):
    """SQLAlchemy model reflecting the new users table (id, name)."""
    __tablename__ = "users"

    id   = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=True)

# ────────────────────────────────────────────────────────────────────────────────
# Pydantic schemas
# ────────────────────────────────────────────────────────────────────────────────
class UserCreate(BaseModel):
    name: str

class UserUpdate(BaseModel):
    name: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    name: Optional[str] = None

    class Config:
        from_attributes = True   # SQLAlchemy → Pydantic conversion

# ────────────────────────────────────────────────────────────────────────────────
# FastAPI app & dependencies
# ────────────────────────────────────────────────────────────────────────────────
app = FastAPI(title="Simple FastAPI CRUD (id & name only)")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ────────────────────────────────────────────────────────────────────────────────
# Health-check
# ────────────────────────────────────────────────────────────────────────────────
@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Verify API & DB connectivity."""
    status_payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "app":      {"status": "healthy", "message": "FastAPI is running"},
        "database": {}
    }
    try:
        db.execute(text("SELECT 1"))
        status_payload["database"] = {
            "status":  "healthy",
            "message": "Database connection is working",
            "type":    "MySQL"
        }
        status_payload["overall_status"] = "healthy"
    except Exception as exc:
        logger.exception("DB health check failed")
        status_payload["database"] = {
            "status":  "unhealthy",
            "message": "Database connection failed",
            "error":   str(exc)
        }
        status_payload["overall_status"] = "unhealthy"
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=status_payload
        )
    return status_payload

# ────────────────────────────────────────────────────────────────────────────────
# CRUD endpoints
# ────────────────────────────────────────────────────────────────────────────────
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=payload.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/", response_model=List[UserResponse])
async def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, updates: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in updates.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

@app.get("/")
async def root():
    return {"message": "FastAPI CRUD App – minimal schema", "docs": "/docs", "health": "/health"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)