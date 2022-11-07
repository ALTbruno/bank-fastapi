from fastapi.testclient import TestClient

def test_health_route(client: TestClient):
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json() == "De boa na lagoa"