import logging
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from starlette import status

from app import APP_NAME
from app.config.database import check_db_connection, DB_CONFIG

logger = logging.getLogger(__name__)

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check():
    """Verify API & DB connectivity"""
    status_payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app": {
            "name": APP_NAME,
            "status": "healthy",
            "message": "FastAPI is running"
        },
        "overall_status": "healthy"
    }

    try:
        check_db_connection()
        status_payload["database"] = {
            "host": DB_CONFIG["host"],
            "status": "healthy",
            "message": "✅ Successfully connected to the Database!",
            "type": "MySQL",
        }
        return status_payload
    except Exception as e:
        logger.exception(e)
        status_payload["database"] = {
            "host": DB_CONFIG["host"],
            "status": "unhealthy",
            "message": "❌ Unable to establish connection with the Database",
            "error": str(e)
        }
        status_payload["overall_status"] = "unhealthy"
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=status_payload
        )