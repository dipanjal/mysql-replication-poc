from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
import uvicorn

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