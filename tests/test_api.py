from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_summarize_endpoint():
    response = client.post(
        "/summarize",
        json={
            "text": (
                "Machine learning is useful. "
                "Python is widely used for machine learning."
            ),
            "summary_length": 1
        }
    )

    assert response.status_code == 200
    assert "summary" in response.json()


def test_empty_text():
    response = client.post(
        "/summarize",
        json={
            "text": "",
            "summary_length": 1
        }
    )

    assert response.status_code == 422