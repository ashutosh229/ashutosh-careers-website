from flask import Flask, jsonify, render_template

app = Flask(__name__)

Jobs = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bangalore, India",
        "salary": 10000
    },
    {
        "id": 2,
        "title": "Front End Enginneer",
        "location": "Delhi, India",
        "salary": 20000
    },
    {
        "id": 3,
        "title": "Backend Enginneer",
        "location": "Bombay, India",
        "salary": 30000
    },
    {
        "id": 4,
        "title": "Cloud Enginneer",
        "location": "bhilai, India",
        "salary": 60000
    },
]


@app.route("/")
def home():
    return render_template("home.html", jobs=Jobs)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
