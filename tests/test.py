import pytest
from http import HTTPStatus
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# -----------------------------
# Basic Endpoint Test
# -----------------------------
def test_api():
    response = client.get("/users/test")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"res": "OK"}


# -----------------------------
# Successful User Creation
# -----------------------------
def test_create_user_success():
    payload = {
        "email": "usmanbutt@usman.com",
        "first_name": "BUTT",
        "last_name": "Muhammad Usman",
        "role": "staff",
        "is_active": True,
        "password_hash": "abcd",
    }

    response = client.post("/users/", json=payload)

    assert response.status_code == HTTPStatus.CREATED


# -----------------------------
# Missing Required Field
# -----------------------------
def test_create_user_missing_email():
    payload = {
        "first_name": "BUTT",
        "last_name": "Muhammad Usman",
        "role": "staff",
        "is_active": True,
        "password_hash": "abcd",
    }

    response = client.post("/users/", json=payload)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


# -----------------------------
# Invalid Email Format
# -----------------------------
def test_create_user_invalid_email():
    payload = {
        "email": "invalid-email",
        "first_name": "BUTT",
        "last_name": "Muhammad Usman",
        "role": "staff",
        "is_active": True,
        "password_hash": "abcd",
    }

    response = client.post("/users/", json=payload)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


# -----------------------------
# Duplicate User Creation
# -----------------------------
def test_create_duplicate_user():
    payload = {
        "email": "duplicate@usman.com",
        "first_name": "Test",
        "last_name": "User",
        "role": "staff",
        "is_active": True,
        "password_hash": "abcd",
    }

    # First creation
    response1 = client.post("/users/", json=payload)
    assert response1.status_code == HTTPStatus.CREATED

    # Second creation (duplicate email)
    response2 = client.post("/users/", json=payload)
    assert response2.status_code in (
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.CONFLICT,
    )


# -----------------------------
# Get User
# -----------------------------
def test_get_user():
    payload = {
        "email": "getuser@usman.com",
        "first_name": "Get",
        "last_name": "User",
        "role": "staff",
        "is_active": True,
        "password_hash": "abcd",
    }

    create_response = client.post("/users/", json=payload)
    assert create_response.status_code == HTTPStatus.CREATED

    # Adjust endpoint if your route is different
    response = client.get(f"/users/{payload['email']}")

    assert response.status_code == HTTPStatus.OK
    assert response.json()["email"] == payload["email"]


# -----------------------------
# Delete User
# -----------------------------
def test_delete_user():
    payload = {
        "email": "delete@usman.com",
        "first_name": "Delete",
        "last_name": "User",
        "role": "staff",
        "is_active": True,
        "password_hash": "abcd",
    }

    create_response = client.post("/users/", json=payload)
    assert create_response.status_code == HTTPStatus.CREATED

    response = client.delete(f"/users/{payload['email']}")

    # Adjust depending on your implementation
    assert response.status_code in (
        HTTPStatus.NO_CONTENT,
        HTTPStatus.OK,
    )
