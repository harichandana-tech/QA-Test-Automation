import sqlite3


DATABASE = "users.db"


# Test 15: Check users table exists
def test_users_table_exists():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name='users'
        """
    )

    table = cursor.fetchone()

    connection.close()

    assert table is not None


# Test 16: Check users table columns
def test_users_table_columns():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute("PRAGMA table_info(users)")

    columns = cursor.fetchall()

    connection.close()

    column_names = [column[1] for column in columns]

    assert "id" in column_names
    assert "name" in column_names
    assert "email" in column_names
    assert "password" in column_names


# Test 17: Check test user exists
def test_test_user_exists():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
        "SELECT * FROM users WHERE email = ?",
        ("qa@test.com",)
    )

    user = cursor.fetchone()

    connection.close()

    assert user is not None


# Test 18: Check email is unique

def test_email_is_unique():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
        """
        SELECT email, COUNT(*)
        FROM users
        GROUP BY email
        HAVING COUNT(*) > 1
        """
    )

    duplicate_email = cursor.fetchone()

    connection.close()

    assert duplicate_email is None