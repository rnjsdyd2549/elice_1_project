from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'Lib_user'
    id = db.Column(db.Integer,  primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.string(10), nullable=False)
    user_id = db.Column(db.String(20), nullable=False, unique=True)
    user_pw = db.Column(db.String(30), nullable=False)

    def __init__(self,user_id,user_pw):
        self.user_id = user_id
        self.user_pw = user_pw