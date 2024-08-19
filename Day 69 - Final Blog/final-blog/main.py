import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from forms import AddForm, RegisterForm, LoginForm, CommentForm
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from functools import wraps
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


class BlogPost(db.Model):
    # one user can have many posts
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # referring the author to the user id
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    # create a reference to User object. The "posts" refers to the posts property in User class
    author = relationship("User", back_populates="posts")

    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    comments = relationship("Comment", back_populates="parent_post")


class User(UserMixin, db.Model):
    # a post and comment can only have one user
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(250), nullable=False)

    # this acts like a list of BlogPost objects attached to each User
    # the "author" refers to the author property in the BlogPost class
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")


class Comment(db.Model):
    # one user can have many comments
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)

    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")


with app.app_context():
    db.create_all()

# ------------------- flask login -------------------
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # if id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


@app.route("/", methods=["GET"])
def home():
    all_posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.title)).scalars().all()
    return render_template("index.html", all_posts=all_posts, current_user=current_user)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if user:
            flash("This email already exists. Log in instead.")
            return redirect(url_for("login"))
        hash_password = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)
        new_user = User()
        new_user.name = form.name.data
        new_user.email = form.email.data
        new_user.password = hash_password

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form=form, current_user=current_user)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if not user:
            flash("This email doesn't exist! Please try again.")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, form.password.data):
            flash("Password incorrect! Please try again.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html", form=form, current_user=current_user)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    form = CommentForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment!")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=form.text.data,
            comment_author=current_user,
            parent_post=post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=post, form=form, current_user=current_user)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def new_post():
    form = AddForm()
    if form.validate_on_submit():
        new_data = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=date.today().strftime("%B %d, %Y"),
            body=form.body.data,
            author=current_user,
            img_url=form.img.data,
        )
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("make-post.html", form=form, current_user=current_user)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def update(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    edit_post = AddForm(
        title=post.title,
        subtitle=post.subtitle,
        img=post.img_url,
        body=post.body,
    )
    if edit_post.validate_on_submit():
        post.title = edit_post.title.data
        post.subtitle = edit_post.subtitle.data
        post.author = current_user
        post.img = edit_post.img.data
        post.body = edit_post.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    return render_template("make-post.html", form=edit_post, is_edit=True, current_user=current_user)


@app.route("/delete/<int:post_id>")
@admin_only
def delete(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=False)
