
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"

# MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "flask_mongodb_assignment")

client = None
collection = None

if MONGODB_URI:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    collection = client[MONGODB_DATABASE]["form_submissions"]


# Task 1: Return JSON data from data.json
@app.route("/api")
def api():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return jsonify(data)
    except (OSError, json.JSONDecodeError):
        app.logger.exception("Unable to read API data")
        return jsonify({"error": "Unable to load API data"}), 500


# Display the form and handle submissions
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            return render_template(
                "index.html",
                error="Please fill in all fields.",
                name=name,
                email=email,
                message=message,
            ), 400

        if collection is None:
            return render_template(
                "index.html",
                error="Database configuration is missing. Check your .env file.",
                name=name,
                email=email,
                message=message,
            ), 500

        try:
            # Check that MongoDB is reachable before inserting
            client.admin.command("ping")

            collection.insert_one({
                "name": name,
                "email": email,
                "message": message,
            })

            return redirect(url_for("success"))

        except Exception:
            app.logger.exception("MongoDB submission failed")
            return render_template(
                "index.html",
                error="Submission failed. Please check the database connection and try again.",
                name=name,
                email=email,
                message=message,
            ), 500

    return render_template("index.html")


# Task 2: Show a separate success page after a successful submission
@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
