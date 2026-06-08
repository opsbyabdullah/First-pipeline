import json
from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_add_task():
    client = app.test_client()

    response = client.post(
        "/tasks",
        data=json.dumps({"title": "Learn GitHub Actions"}),
        content_type="application/json",
    )

    assert response.status_code == 404
