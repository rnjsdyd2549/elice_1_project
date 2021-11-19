from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Lib_User(db.Model):

    __tablename__ = 'Lib_user'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.String(30), nullable=False, unique=True)
    user_pw = db.Column(db.String(100), nullable=False)

    def __init__(self, user_name, user_id,user_pw):
        self.user_name = user_name
        self.user_id = user_id
        self.user_pw = user_pw

class book_info(db.Model):
    __tablename__ ='tb_book_info'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_name = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    publication_date = db.Column(db.String(20), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    isbs = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    link = db.Column(db.String(55), nullable=False)

    def __init__(self, book_name, publisher, author, publication_date, pages, isbs, description, link):
        self.book_name = book_name
        self.publisher = publisher
        self. author = author
        self.publication_date = publication_date
        self.pages = pages
        self.isbs = isbs
        self.description = description
        self.link = link