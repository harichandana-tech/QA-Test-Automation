import sqlite3
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


BASE_URL = "http://127.0.0.1:5000"


# Create a test user before running the tests
@pytest.fixture(scope="session", autouse=True)
def create_test_user():

    connection = sqlite3.connect("users.db")

    try:
        connection.execute(
            """
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
            """,
            ("QA Tester", "qa@test.com", "Test@123")
        )
        connection.commit()

    except sqlite3.IntegrityError:
        # User already exists
        pass

    connection.close()


# Create a fresh browser for each test
@pytest.fixture
def browser():

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


# Test 1: Valid Login
def test_valid_login(browser):

    browser.get(BASE_URL + "/login")

    browser.find_element(By.NAME, "email").send_keys("qa@test.com")
    browser.find_element(By.NAME, "password").send_keys("Test@123")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    heading = browser.find_element(By.TAG_NAME, "h1").text

    assert heading == "Login Successful"


# Test 2: Invalid Password
def test_invalid_password(browser):

    browser.get(BASE_URL + "/login")

    browser.find_element(By.NAME, "email").send_keys("qa@test.com")
    browser.find_element(By.NAME, "password").send_keys("WrongPassword")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "Invalid email or password." in browser.page_source


# Test 3: Invalid Email
def test_invalid_email(browser):

    browser.get(BASE_URL + "/login")

    browser.find_element(By.NAME, "email").send_keys("wrong@test.com")
    browser.find_element(By.NAME, "password").send_keys("Test@123")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "Invalid email or password." in browser.page_source


# Test 4: Empty Email
def test_empty_email(browser):

    browser.get(BASE_URL + "/login")

    browser.find_element(By.NAME, "password").send_keys("Test@123")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    email_field = browser.find_element(By.NAME, "email")

    assert email_field.get_attribute("value") == ""


# Test 5: Empty Password
def test_empty_password(browser):

    browser.get(BASE_URL + "/login")

    browser.find_element(By.NAME, "email").send_keys("qa@test.com")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # User should remain on the login page
    assert "/login" in browser.current_url

# -----------------------------
# REGISTRATION TESTS
# -----------------------------

# Test 6: Successful Registration
def test_successful_registration(browser):

    browser.get(BASE_URL + "/register")

    unique_email = f"newuser{int(time.time())}@test.com"

    browser.find_element(By.NAME, "name").send_keys("New QA User")
    browser.find_element(By.NAME, "email").send_keys(unique_email)
    browser.find_element(By.NAME, "password").send_keys("Test@123")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "Registration successful!" in browser.page_source


# Test 7: Duplicate Email
def test_duplicate_email(browser):

    browser.get(BASE_URL + "/register")

    browser.find_element(By.NAME, "name").send_keys("Duplicate User")
    browser.find_element(By.NAME, "email").send_keys("qa@test.com")
    browser.find_element(By.NAME, "password").send_keys("Test@123")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "Email already exists." in browser.page_source


# Test 8: Empty Name
def test_empty_name(browser):

    browser.get(BASE_URL + "/register")

    browser.find_element(By.NAME, "email").send_keys("emptyname@test.com")
    browser.find_element(By.NAME, "password").send_keys("Test@123")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "/register" in browser.current_url


# Test 9: Empty Email
def test_empty_registration_email(browser):

    browser.get(BASE_URL + "/register")

    browser.find_element(By.NAME, "name").send_keys("Empty Email User")
    browser.find_element(By.NAME, "password").send_keys("Test@123")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "/register" in browser.current_url


# Test 10: Empty Password
def test_empty_registration_password(browser):

    browser.get(BASE_URL + "/register")

    browser.find_element(By.NAME, "name").send_keys("Empty Password User")
    browser.find_element(By.NAME, "email").send_keys("emptypassword@test.com")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "/register" in browser.current_url