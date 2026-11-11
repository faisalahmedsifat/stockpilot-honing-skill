from fastapi.testclient import TestClient

from app.main import create_app

def test_create_app():
    app = create_app()
    
    assert app is not None
    assert app.title == "StockPilot"
    
def test_health_live():
    app = create_app()
    client = TestClient(app)
    
    response = client.get("/health/live")
    
    assert response.status_code == 200
    assert response.json() == {'status': 'live'}
    
def test_health_ready():
    app = create_app()
    client = TestClient(app)

    response = client.get("/health/ready")
    
    assert response.status_code == 200
    assert response.json() == {'status': 'ready'}