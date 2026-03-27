# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Flask App is Running in Docker!</h1>"

if __name__ == "__main__":
    # Ensure the app runs on 0.0.0.0 to be accessible within a container
    app.run(host="0.0.0.0", port=8080)
