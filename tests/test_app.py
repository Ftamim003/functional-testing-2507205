
import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Function Testing" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert "commit_sha" in data


def test_run_function_success(client):
    response = client.post(
        "/api/run",
        json={
            "function": "is_adult",
            "arguments": {"age": 20}
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
    assert data["result"] is True
    assert data["result_type"] == "bool"


def test_run_function_error(client):
    response = client.post(
        "/api/run",
        json={
            "function": "divide",
            "arguments": {"a": 10, "b": 0}
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] is False
    assert data["error_type"] == "ZeroDivisionError"


def test_invalid_function(client):
    response = client.post(
        "/api/run",
        json={
            "function": "unknown_function",
            "arguments": {}
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] is False
    assert data["error_type"] == "InvalidFunction"


def test_invalid_arguments(client):
    response = client.post(
        "/api/run",
        json={
            "function": "is_adult",
            "arguments": []
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] is False
    assert data["error_type"] == "InvalidArguments"


def test_invalid_json_request(client):
    response = client.post(
        "/api/run",
        data="invalid json",
        content_type="application/json"
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] is False
    assert data["error_type"] == "InvalidRequest"
