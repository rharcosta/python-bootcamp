from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

# JINJA TEMPLATE
app = Flask(__name__)


@app.route("/")
def home():
    random_number = randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("age-gender.html", person_name=name, person_gender=gender, years=age)


@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=response)


if __name__ == "__main__":
    app.run(debug=True)
