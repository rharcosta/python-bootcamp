import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from forms import AddForm
# python -m pip install -r requirements.txt

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["FLASK_KEY"]
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_URI"]
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Portfolio(db.Model):
    __tablename__ = "project_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
def home():
    all_projects = db.session.execute(db.select(Portfolio)).scalars().all()
    return render_template("index.html", all_projects=all_projects)


@app.route("/project/<int:project_id>", methods=["GET", "POST"])
def show_project(project_id):
    project = db.session.execute(db.select(Portfolio).where(Portfolio.id == project_id)).scalar()
    return render_template("project.html", project=project)


@app.route("/new-project", methods=["GET", "POST"])
def new_project():
    form = AddForm()
    if form.validate_on_submit():
        new_data = Portfolio(
            title=form.title.data,
            body=form.body.data,
            img_url=form.img.data,
        )
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("make-post.html", form=form)


@app.route("/edit-project/<int:project_id>", methods=["GET", "POST"])
def update(project_id):
    project = db.session.execute(db.select(Portfolio).where(Portfolio.id == project_id)).scalar()
    edit_project = AddForm(
        title=project.title,
        body=project.body,
        img=project.img_url,
    )
    if edit_project.validate_on_submit():
        project.title = edit_project.title.data
        project.body = edit_project.body.data
        project.img = edit_project.img.data
        db.session.commit()
        return redirect(url_for("show_post", project_id=project_id))
    return render_template("make-post.html", form=edit_project, is_edit=True)


@app.route("/delete/<int:project_id>")
def delete(project_id):
    project = db.session.execute(db.select(Portfolio).where(Portfolio.id == project_id)).scalar()
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=False, port=5055)
