from sqlalchemy.orm import defaultload
from main import db
from datetime import *

class book_info(db.Model):
    __tablename__ = 'book_info'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_name = db.Column(db.String(100))
    publisher = db.Column(db.String(50))
    author = db.Column(db.String(50))
    publication_date = db.Column(db.Date)
    pages = db.Column(db.Integer)
    isbn = db.Column(db.String(50))
    description = db.Column(db.Text)
    link = db.Column(db.String(100))
    stack = db.Column(db.Integer, default=10)
    score = db.Column(db.Integer)
    img_path = db.Column(db.Text)

    def __init__(self, id, book_name, publisher, author, publication_date, pages, isbs, description, link, stack, score, img_path):
        self.id = id
        self.book_name = book_name
        self.publisher = publisher
        self.author = author
        self.publication_date = publication_date
        self.pages = pages
        self.isbs = isbs
        self.description = description
        self.link = link
        self.stack = stack
        self.score = score
        self.img_path = img_path


class LibUser(db.Model):
    __tablename__ = 'LibUser'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(50))

    # def __init__(self, id, email, name, password):
    #     self.id = id
    #     self.email = email
    #     self.name = name
    #     self.password = password

class book_rent(db.Model):
    __tablename__ = 'book_rent'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey(book_info.id), nullable=False)
    user_email = db.Column(db.String(100), db.ForeignKey(LibUser.user_email), nullable=False)

    rent_date = db.Column(db.Date, default = date.today())
    rent_end = db.Column(db.Date, default = date.today() + timedelta(days=7))

    return_date = db.Column(db.Date)

    def __init__(self, id, book_id, user_email, rent_date=None, rent_end=None, return_date=None):
        self.id = id
        self.book_id = book_id
        self.user_email = user_email
        self.rent_date = rent_date
        self.rent_end = rent_end
        self.return_date = return_date 

class book_review(db.Model):
    __tablename__ = 'book_review'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey(book_info.id), nullable=False)
    user_email = db.Column(db.String(100), db.ForeignKey(LibUser.user_email), nullable=False)
    score = db.Column(db.Float, nullable=False)
    review = db.Column(db.Text())