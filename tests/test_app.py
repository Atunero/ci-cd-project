import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test for the / route."""
    rv = client.get('/')
    assert b'Hello, World!' in rv.data
