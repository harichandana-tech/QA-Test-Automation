from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "qa-test-secret-key"


# -----------------------------
# Database Connection
# -----------------------------
def get_db_connection():
    connection = sqlite3.connect("users.db")
    connection.row_factory = sqlite3.Row
    return connection


# -----------------------------
# Create Database
# -----------------------------
def create_database():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# -----------------------------
# Home / Login
# -----------------------------
@app.route("/")
def home():
    return redirect(url_for("login"))


# -----------------------------
# Login
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        connection = get_db_connection()

        user = connection.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?",
            (email, password)
        ).fetchone()

        connection.close()

        if user:
            return f"""
                <h1>Login Successful</h1>
                <p>Welcome, {user["name"]}!</p>
                <a href="/login">Logout</a>
            """

        flash("Invalid email or password.")

    return render_template("login.html")


# -----------------------------
# Registration
# -----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        if not name or not email or not password:
            flash("All fields are required.")
            return render_template("register.html")

        connection = get_db_connection()

        try:
            connection.execute(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (name, email, password)
            )

            connection.commit()
            connection.close()

            flash("Registration successful! Please login.")
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            connection.close()
            flash("Email already exists.")

    return render_template("register.html")


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    create_database()
    app.run(debug=True)