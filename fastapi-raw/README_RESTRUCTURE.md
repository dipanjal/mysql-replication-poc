# FastAPI Raw SQL - Restructured Architecture

This directory has been restructured to follow a layered architecture pattern similar to `fastapi-app`, separating concerns into distinct layers.

## New Structure

```
fastapi-raw/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config/
│   │   ├── __init__.py
│   │   └── database.py         # Database configuration and connection management
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── health_controller.py # Health check endpoints
│   │   └── user_controller.py   # User CRUD endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py     # Business logic layer
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── user_repository.py  # Data access layer with raw SQL
│   └── schemas/
│       ├── __init__.py
│       └── user.py             # Pydantic models for request/response
├── backup/                     # Original files backed up here
├── helper.py                   # Utility functions (unchanged)
├── requirements.txt
├── Dockerfile                  # Updated to use new app structure
└── docker-compose.yml
```

## Architecture Layers

### 1. Controllers Layer (`app/controllers/`)
- **Purpose**: Handle HTTP requests and responses
- **Responsibilities**: 
  - Route definition
  - Request validation
  - Response formatting
  - Error handling
- **Files**: `health_controller.py`, `user_controller.py`

### 2. Services Layer (`app/services/`)
- **Purpose**: Business logic and orchestration
- **Responsibilities**:
  - Business rules
  - Data transformation
  - Service coordination
- **Files**: `user_service.py`

### 3. Repositories Layer (`app/repositories/`)
- **Purpose**: Data access and persistence
- **Responsibilities**:
  - Database operations
  - Raw SQL queries
  - Data mapping
- **Files**: `user_repository.py`

### 4. Schemas Layer (`app/schemas/`)
- **Purpose**: Data models and validation
- **Responsibilities**:
  - Request/response models
  - Data validation
  - API documentation
- **Files**: `user.py`

### 5. Config Layer (`app/config/`)
- **Purpose**: Configuration management
- **Responsibilities**:
  - Database configuration
  - Connection management
  - Environment variables
- **Files**: `database.py`

## Key Changes

1. **Separation of Concerns**: Each layer has a specific responsibility
2. **Dependency Injection**: Services depend on repositories, controllers depend on services
3. **Raw SQL**: Maintains the original raw SQL approach while adding structure
4. **Error Handling**: Consistent error handling across layers
5. **Type Safety**: Full type hints and Pydantic models

## Running the Application

```bash
# Using uvicorn directly
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Using Docker
docker-compose up --build

# Using Makefile
make run
```

## Testing

```bash
# Run the test script
python test_restructure.py
```

## Migration Notes

- Original `main.py` and `db.py` are backed up in `backup/` directory
- All functionality preserved with improved structure
- Dockerfile updated to use new app structure
- Helper functions remain unchanged for compatibility 