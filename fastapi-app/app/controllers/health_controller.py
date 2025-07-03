from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.config.database import get_db
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["health"])

@router.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Verify API & DB connectivity"""
    status_payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app": {"status": "healthy", "message": "FastAPI is running"},
        "database": {}
    }
    
    try:
        db.execute(text("SELECT 1"))
        status_payload["database"] = {
            "status": "healthy",
            "message": "Database connection is working",
            "type": "MySQL",
        }
        status_payload["overall_status"] = "healthy"
        return status_payload
    except Exception as exc:
        logger.exception("DB health check failed")
        status_payload["database"] = {
            "status": "unhealthy",
            "message": "Database connection failed",
            "error": str(exc)
        }
        status_payload["overall_status"] = "unhealthy"
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=status_payload
        )

@router.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "FastAPI CRUD App for ProxySQL – minimal schema",
        "docs": "/docs",
        "health": "/health"
    }
