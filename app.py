from flask import Flask, render_template, request, redirect, url_for
from authenticator import Authenticator

app = Flask(__name__)
authenticator = Authenticator()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        action = request.form.get("action")

        if action == "Login":
            if authenticator.authenticate(username, password):
                return redirect(url_for('image'))
            else:
                message = "Invalid credentials. Please try again."
        elif action == "Register":
            message = authenticator.register(username, password)

    return render_template("index.html", message=message)

@app.route("/image")
def image():
    return render_template("image.html")

if __name__ == "__main__":
    app.run(debug=True)
