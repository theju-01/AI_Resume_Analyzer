from flask import Flask, render_template, request
from model import analyze_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        resume_text = request.form["resume_text"]
        result = analyze_resume(resume_text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)