"""This is a test for api test"""
from app import app


def test_app():
    """Testing api from flask"""
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.data == b"Hello world!"
