# FastAPI POC

A basic FastAPI application for MySQL replication POC.

## Features

- RESTful API with CRUD operations for users to test ProxySQL routing
- Health check endpoint
- Automatic API documentation

## Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /users` - Get all users
- `GET /users/{user_id}` - Get user by ID
- `POST /users` - Create new user
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

## Installation

### Using Makefile (Recommended)

```bash
# Clean up environment
make clean

# Install dependencies and setup virtual environment
make install

# Clean and Build dependencies
make clean install

# Start the application in development mode
make run
```

## API Documentation

Once the application is running, you can access:

- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc
- OpenAPI schema: http://localhost:8000/openapi.json

## Example Usage

```bash
# Create a user
curl -X POST "http://localhost:8000/users" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com", "age": 30}'

# Get all users
curl "http://localhost:8000/users"

# Get a specific user
curl "http://localhost:8000/users/1"

# Update a user
curl -X PUT "http://localhost:8000/users/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Updated", "email": "john.updated@example.com", "age": 31}'

# Delete a user
curl -X DELETE "http://localhost:8000/users/1"
``` 