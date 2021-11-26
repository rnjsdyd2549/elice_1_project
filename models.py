from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Lib_User(db.Model):

    __tablename__ = 'Lib_user'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, primary_key=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(30))

    def __init__(self, email, name, password):
        self.email = email
        self.password = password
        self.name = name

class Book(db.Model):
    __tablename__ ='book'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_name = db.Column(db.String(128))
    publisher = db.Column(db.String(128))
    author = db.Column(db.String(30))
    publication_date = db.Column(db.Date)
    pages = db.Column(db.Integer)
    isbs = db.Column(db.String(255))
    description = db.Column(db.Text)
    link = db.Column(db.String(255))
    stack = db.Column(db.Integer)

    def __init__(self, book_name, publisher, author, publication_date, pages, isbs, description, link, stack):
        self.book_name = book_name
        self.publisher = publisher
        self.author = author
        self.publication_date = publication_date
        self.pages = pages
        self.isbs = isbs
        self.description = description
        self.link = link
        self.stack = stack

class Rent_user(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('Book_info.id'))
    user_id =db.Column(db.Integer, db.ForeignKey('Lib_User.id'))
    rent_date = db.Column(db.Date)
    return_date = db.Column(db.Date, nullable=True, default=None)

    def __init__(self, rent_date, retrun_date):
        self.rent_date = rent_date
        self.return_date = retrun_date

    

class Book_comment(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book_info.id'))
    user_id =db.Column(db.Integer, db.ForeignKey('Lib_User.id'))
    content = db.Column(db.Text)
    rating = db.Column(db.Integer)
    