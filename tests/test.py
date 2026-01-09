from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/users",
        
    )

    assert response.status_code == 200
    assert response.json() == {
        "name": "apple",
        "price": 10.0,
        "total_with_tax": 11.0
    }
