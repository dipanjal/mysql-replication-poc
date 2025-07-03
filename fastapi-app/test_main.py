from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "docs" in data
    assert "health" in data

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "timestamp" in data
    assert "app" in data
    assert "database" in data
    assert "overall_status" in data

def test_create_user():
    """Test user creation"""
    user_data = {"name": "John Doe"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == user_data["name"]
    assert "id" in data

def test_get_users():
    """Test getting all users"""
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user():
    """Test getting a specific user"""
    # First create a user
    user_data = {"name": "Jane Doe"}
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    # Then get the user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["id"] == user_id

def test_get_nonexistent_user():
    """Test getting a user that doesn't exist"""
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_update_user():
    """Test updating a user"""
    # First create a user
    user_data = {"name": "Original Name"}
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    # Then update the user
    update_data = {"name": "Updated Name"}
    response = client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["id"] == user_id

def test_delete_user():
    """Test deleting a user"""
    # First create a user
    user_data = {"name": "To Delete"}
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    # Then delete the user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204
    
    # Verify user is deleted
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404 