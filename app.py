from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

users = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users[username] = password
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        return "Invalid Credentials"
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", username=session["user"])
    return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

img
