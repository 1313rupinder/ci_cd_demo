from app import app, add, is_even

def test_add():
    assert add(2, 3) == 5

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"running" in response.data
