
import pytest
from app import app, students, attendance

@pytest.fixture
def client():
    students.clear()
    students.extend(["Rahul", "Priya", "Amit"])
    attendance.clear()

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_student(client):
    response = client.post(
        "/add",
        data={"name": "Anushka"}
    )
    assert response.status_code == 302
    assert "Anushka" in students


def test_mark_attendance(client):
    response = client.post(
        "/mark",
        data={"name": "Rahul", "status": "Present"}
    )
    assert response.status_code == 302
    assert attendance["Rahul"] == "Present"


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
