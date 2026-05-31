from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message" : "The server is online"}

def test_get_calls():
    response = client.get("/calls")
    assert response.status_code == 200
    calls = response.json()["calls"]
    assert isinstance(calls, list)
    assert all(not call["is_archived"] for call in calls)

def test_get_calls_invalid_filter():
    response = client.get("/calls?call_type=test")
    assert response.status_code == 400

def test_get_call_by_the_id():
    response = client.get("/calls/3ff887f9-1812-4497-850e-3e41faaa0c56")
    assert response.status_code == 200
    assert response.json()["id"] == "3ff887f9-1812-4497-850e-3e41faaa0c56"
    assert response.json()["call_type"] == "missed"

    response = client.get("/calls/-1")
    assert response.status_code == 404

def test_archive_call_by_id():
    response = client.patch("/calls/3ff887f9-1812-4497-850e-3e41faaa0c56/archive")
    assert response.status_code == 200
    assert response.json()["is_archived"] == True

    response = client.patch("/calls/1812-4497-850e-3e41faaa0c56/archive")
    assert response.status_code == 404

def test_unarchive_call_by_id():
    response = client.patch("/calls/3ff887f9-1812-4497-850e-3e41faaa0c56/unarchive")
    assert response.status_code == 200
    assert response.json()["is_archived"] == False

    response = client.patch("/calls/1812-4497-850e-3e41faaa0c56/unarchive")
    assert response.status_code == 404

def test_add_note():
    response = client.post(
        "/calls/3ff887f9-1812-4497-850e-3e41faaa0c56/notes",
        json={"content": "Test Note"}
    )
    assert response.status_code == 200
    assert any(n["content"] == "Test Note" for n in response.json()["notes"])

    response = client.post("/calls/999/notes", json={"content": "Test Note"})
    assert response.status_code == 404

def test_update_note():
    response = client.patch(
        "/calls/3ff887f9-1812-4497-850e-3e41faaa0c56/notes/62648180-4fb9-462f-80fc-fe51c2337a82",
        json={"content": "Updated content"}
    )
    assert response.status_code == 200
    assert response.json()["content"] == "Updated content"
    assert response.json()["id"] == "62648180-4fb9-462f-80fc-fe51c2337a82"

    response = client.patch(
        "/calls/3ff887f9-1812-4497-850e-3e41faaa0c56/notes/nonexistent-note-id",
        json={"content": "Updated content"}
    )
    assert response.status_code == 404

def test_create_call():
    response = client.post("/calls", json={
        "direction": "inbound",
        "call_type": "missed",
        "duration": 0,
        "is_archived": False,
        "from_": "69 55 555 556",
        "to_": "699 99 999 994"
    })
    assert response.status_code == 200
    assert response.json()["direction"] == "inbound"
    assert response.json()["call_type"] == "missed"
    assert "id" in response.json()

    response = client.post("/calls", json={
        "direction": "txt",
        "call_type": "tst",
        "duration": -1,
        "is_archived": True,
        "from_": "69 55",
        "to_": "699 9"
    })
    assert response.status_code == 400


    