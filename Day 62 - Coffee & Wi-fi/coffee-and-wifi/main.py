from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

'''
This will install the packages from requirements.txt for this project.

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt
'''

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label="Cafe name", validators=[DataRequired()])
    location = StringField(label="Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open_time = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired()])
    close_time = StringField(label="Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", validators=[DataRequired()], choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi_rating = SelectField(label="Wi-fi Strength Rating", validators=[DataRequired()], choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power_rating = SelectField(label="Power Socket Availability", validators=[DataRequired()], choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding="utf-8") as file:
            # Cafe Name, Location, Open, Close, Coffee, Wi-fi, Power
            file.write(f"\n{form.cafe.data},"
                       f"{form.location.data},"
                       f"{form.open_time.data},"
                       f"{form.close_time.data},"
                       f"{form.coffee_rating.data},"
                       f"{form.wifi_rating.data},"
                       f"{form.power_rating.data}")
        return redirect(url_for("all_cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def all_cafes():
    with open("cafe-data.csv", newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
