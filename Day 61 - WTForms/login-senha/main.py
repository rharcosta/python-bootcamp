from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

'''
This will install the packages from requirements.txt for this project.

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

Email Validator:
pip install email-validator  or
Settings -> Project -> Python Interpreter -> + -> email-validator

Bootstrap:
pip install bootstrap-flask
'''


class LoginForm(FlaskForm):
    # DataRequired: make required fields
    # Terminal: pip install wtforms[email]
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "nina"
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():  # validate fields (post)
        # print(login_form.email.data) -> will print the data
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
