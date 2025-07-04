import logging
from contextlib import asynccontextmanager
from datetime import datetime, timezone

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Import controllers
from app.controllers import health_controller, user_controller

# ────────────────────────────────────────────────────────────────────────────────
# Logging
# ────────────────────────────────────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ────────────────────────────────────────────────────────────────────────────────
# Lifespan
# ────────────────────────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup
    print("Server listening...")
    yield
    # Shutdown
    print("Shutting down...")

# ────────────────────────────────────────────────────────────────────────────────
# FastAPI app
# ────────────────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="User Management API",
    description="A FastAPI application with MySQL using raw SQL queries and layered architecture",
    version="1.0.0",
    lifespan=lifespan
)

# ────────────────────────────────────────────────────────────────────────────────
# Global Exception Handler
# ────────────────────────────────────────────────────────────────────────────────
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for unhandled exceptions"""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "message": "An unexpected error occurred",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "path": str(request.url)
        }
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handler for HTTP exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "path": str(request.url)
        }
    )

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ────────────────────────────────────────────────────────────────────────────────
# Include routers
# ────────────────────────────────────────────────────────────────────────────────
app.include_router(health_controller.router)
app.include_router(user_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 