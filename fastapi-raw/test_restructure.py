#!/usr/bin/env python3
"""Test script to verify the restructured FastAPI application"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app
from fastapi.testclient import TestClient

def test_health_endpoint():
    """Test the health endpoint"""
    client = TestClient(app)
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.json()
    assert "application" in data
    assert "database" in data
    print("✅ Health endpoint test passed")

def test_users_endpoint():
    """Test the users endpoint"""
    client = TestClient(app)
    response = client.get("/users")
    assert response.status_code == 200
    print("✅ Users endpoint test passed")

if __name__ == "__main__":
    print("Testing restructured FastAPI application...")
    test_health_endpoint()
    test_users_endpoint()
    print("🎉 All tests passed! The restructured application is working correctly.") 