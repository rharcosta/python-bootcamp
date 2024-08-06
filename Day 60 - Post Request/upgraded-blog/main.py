from flask import Flask, render_template, request
from dotenv import load_dotenv
from os import environ
import requests
import smtplib

load_dotenv()
app = Flask(__name__)
data = requests.get("https://api.npoint.io/7dead3dca7cda56263c4").json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=data)


@app.route("/post/<int:index>")
def show_post(index):
    for posts in data:
        if posts['id'] == index:
            return render_template("post.html", post=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        send_email()
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email():
    email = environ["BLOG_EMAIL"]
    password = environ["BLOG_PASSWORD"]
    smtp_address = environ["SMTP_ADDRESS"]
    name = request.form["name"]
    email_person = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email,
                            msg=f"Subject: New Contact\n\n"
                                f"Name: {name}\n"
                                f"Email: {email_person}\n"
                                f"Phone: {phone}\n"
                                f"Message: {message}")


if __name__ == "__main__":
    app.run(debug=True)
