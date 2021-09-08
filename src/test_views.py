from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_get_home():
    response = client.get("/") # requests.get("") # python requests
    assert response.status_code == 200
    assert  "application/json" == response.headers['content-type']
