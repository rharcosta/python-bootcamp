# SQLAlchemy is defined as an ORM (Object Relational Mapping)
# pip3 install -r requirements.txt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# TODO 1: create the database
class Base(DeclarativeBase):
    pass


# TODO 2: create the extension
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"  # table name
db.init_app(app)  # initialize the app


# TODO 3: setting columns
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[str] = mapped_column(Float, nullable=False)

    # optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f'<Book {self.title}>'


# TODO 4: create tables
with app.app_context():
    db.create_all()

# TODO: CRUD data records (Create, Read, Update, Delete)

# TODO: CREATE
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# TODO: READ ALL RECORDS
with app.app_context():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()

# TODO: READ A PARTICULAR RECORD
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

# TODO: UPDATE A PARTICULAR RECORD
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# TODO: DELETE A PARTICULAR RECORD BY PRIMARY KEY
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
