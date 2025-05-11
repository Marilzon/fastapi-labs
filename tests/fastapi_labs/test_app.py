from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_labs.app import app


def test_root_returns_string():
    # Arranje
    client = TestClient(app)

    # Act
    response = client.get("/")
    expected_message = {"message": "fastapi_labs works!"}
    expected_http_status = HTTPStatus.OK

    # Assert
    assert response.json() == expected_message
    assert response.status_code == expected_http_status
