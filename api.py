from flask import Blueprint, jsonify, render_template, request
import sqlite3 as sql
from db_connect import db

from models import Lib_User
bp = Blueprint('bp', __name__)

@bp.route('/')
def home_login():
    return render_template('index.html')

@bp.route('/join')
def register():
    return render_template('join.html')

@bp.route('/join', methods=['POST'])
def adduser():
    userName = request.form['userName']
    userId = request.form['userId']
    userPw = request.form['userPw']

    user = Lib_User(userName, userId, userPw)
    db.session.add(user)
    db.session.commit()
    return jsonify({"result": "success"})
    
@bp.route('/main')
def main():
    with sql.connect('tb_book_info.db') as con:
        cur =con.cursor()
        cur.execute('SELECT * FROM tb_book_info')
        result = cur.fetchall()
        print(result)
    return render_template('main.html')