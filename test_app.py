from app import add, is_even

def test_add():
    assert add(2, 3) == 6

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
