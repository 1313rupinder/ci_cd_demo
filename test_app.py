from app import app, add, is_even


def post_calculation(num1, num2, operation):
    client = app.test_client()
    return client.post(
        "/", data={"num1": num1, "num2": num2, "operation": operation}
    )


def test_add():
    assert add(2, 3) == 5


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False


def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Calculator" in response.data


def test_calculator_add():
    response = post_calculation("2", "3", "add")
    assert b"Result: <strong>5.0</strong>" in response.data


def test_calculator_subtract():
    response = post_calculation("10", "4", "subtract")
    assert b"Result: <strong>6.0</strong>" in response.data


def test_calculator_multiply():
    response = post_calculation("6", "7", "multiply")
    assert b"Result: <strong>42.0</strong>" in response.data


def test_calculator_divide():
    response = post_calculation("10", "4", "divide")
    assert b"Result: <strong>2.5</strong>" in response.data


def test_calculator_divide_by_zero():
    response = post_calculation("5", "0", "divide")
    assert b"Cannot divide by zero!" in response.data
    assert b"Result:" not in response.data


def test_calculator_invalid_input():
    response = post_calculation("abc", "3", "add")
    assert b"Please enter valid numbers." in response.data