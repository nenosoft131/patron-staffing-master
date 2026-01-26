import pytest
from http import HTTPStatus
from app.helper.utils import calcaulte_eligibility
from fastapi.testclient import TestClient
from main import app
# def test_check_eligibilty():
#     out = calcaulte_eligibility(35,30000,"Gov")
    
#     assert out == True
    
    
# def test_check_ineligibilty():
#     out = calcaulte_eligibility(30,30000,"Gov")
    
#     assert out == False
    
client = TestClient(app)

def test_api():
    response = client.get("/users/test")
    assert response.status_code == 200
    assert response.json() == {'res': 'OK'}

def test_create_user():
    
    payload = {
            'email' : 'usmanbutt@usman.com',
            'first_name' : 'BUTT',
            'last_name' : 'Muhammad Usman',
            'role' : 'staff',
            'is_active' : True,
            'password_hash' : 'abcd'
    }
    response = client.post("/users/", json=payload)
    
    assert response.status_code == HTTPStatus.CREATED