from flask import Flask

# on terminal: set FLASK_APP=main.py (name of the file)
# flask --app main (name of the file) run
# running on: http://127.0.0.1:5000

app = Flask(__name__)


@app.route("/")  # python decorator: a function that modifies a function
def hello_world():
    return ('<h1>Hello, World!</h1>'
            '<iframe src="https://giphy.com/embed/Ok4HaWlYrewuY" width="400" height="400" </iframe>')


@app.route("/bye")
def say_bye():
    return "Bye!"


@app.route("/username/<name>")
def greetings(name):
    return f"Welcome {name}!"


if __name__ == "__main__":
    # debug=True : it will refresh again everytime I modify my program
    app.run(debug=True)
