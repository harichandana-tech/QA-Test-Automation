import requests

BASE_URL = "http://127.0.0.1:5000"


# Test 11: Login page API
def test_login_page_api():

    response = requests.get(BASE_URL + "/login")

    assert response.status_code == 200
    assert "Login" in response.text


# Test 12: Registration page API
def test_register_page_api():

    response = requests.get(BASE_URL + "/register")

    assert response.status_code == 200
    assert "Register" in response.text


# Test 13: Home page redirects to Login
def test_home_redirect():

    response = requests.get(
        BASE_URL + "/",
        allow_redirects=False
    )

    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


# Test 14: Invalid URL
def test_invalid_url():

    response = requests.get(BASE_URL + "/invalid-page")

    assert response.status_code == 404