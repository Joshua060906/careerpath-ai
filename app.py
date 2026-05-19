from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model

with open("career_model.pkl", "rb") as f:
    model = pickle.load(f)

career_map = {

    0: "Software Engineer",
    1: "Data Scientist",
    2: "Cyber Security Analyst",
    3: "UI/UX Designer",
    4: "Cloud Engineer",
    5: "Digital Marketer",
    6: "AI Engineer",
    7: "Business Analyst",
    8: "DevOps Engineer",
    9: "Graphic Designer",
    10: "Web Developer",
    11: "Mobile App Developer",
    12: "Database Administrator",
    13: "Network Engineer",
    14: "Game Developer",
    15: "Content Writer",
    16: "Machine Learning Engineer",
    17: "Product Manager",
    18: "Blockchain Developer",
    19: "Ethical Hacker"

}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    name = request.form["name"]

    marks = float(request.form["marks"])

    coding = float(request.form["coding"])

    communication = float(request.form["communication"])

    features = [[marks, coding, communication]]

    prediction = model.predict(features)[0]

    career = career_map[prediction]

    return render_template(
        "result.html",
        name=name,
        career=career
    )

if __name__ == "__main__":
    app.run(debug=True)