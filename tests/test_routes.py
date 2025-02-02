import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_extract_symbol(client):
    response = client.post("/api/extract-symbol", json={"query": "symbol for Tesla"})
    assert response.status_code == 200
    assert "symbol" in response.json


def test_fetch_financials(client):
    response = client.post("/api/fetch-financials", json={"ticker": "TSLA"})
    assert response.status_code == 200
    assert "file" in response.json


def test_analyze_stock(client):
    response = client.post(
        "/api/analyze-stock",
        json={"file_path": "TSLA.json", "query": "Analyze this stock"},
    )
    assert response.status_code == 200
    assert "analysis" in response.json
