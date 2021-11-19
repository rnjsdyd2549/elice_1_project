from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Lib_User(db.Model):

    __tablename__ = 'Lib_user'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_name = db.Column(db.string(10), nullable=False)
    user_id = db.Column(db.String(30), nullable=False, unique=True)
    user_pw = db.Column(db.String(30), nullable=False)

    def __init__(self, user_name, user_id,user_pw):
        self.user_name = user_name
        self.user_id = user_id
        self.user_pw = user_pw

class book_info(db.Model):
    __tablename__ ='tb_book_info'
    