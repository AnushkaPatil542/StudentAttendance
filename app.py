
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []
attendance = {}

@app.route("/")
def home():
    return render_template(
        "index.html",
        students=students,
        attendance=attendance
    )

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name")

    if name and name.strip():
        students.append(name.strip())

    return redirect("/")

@app.route("/mark", methods=["POST"])
def mark_attendance():
    name = request.form.get("name")
    status = request.form.get("status")

    if name in students and status in ["Present", "Absent"]:
        attendance[name] = status

    return redirect("/")

@app.route("/health")
def health():
    return {"status": "OK"}, 200

if __name__ == "__main__":
    app.run(debug=True)
