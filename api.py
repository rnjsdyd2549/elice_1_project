from flask import Blueprint, jsonify, render_template, request
import sqlite3 as sql
bp = Blueprint('bp', __name__)

@bp.route('/')
def home_login():
    return render_template('index.html')

@bp.route('/join')
def register():
    return render_template('join.html')

@bp.route('/join', method=['POST'])
def adduser():
    name =request.form['name']
    userId = request.form['userId']
    userPw = request.form['userPw']
    userPw2 = request.form['userPw2']

    with sql.connect('tb_book_info.db') as con:
        cur =con.cursor()
        cur.execute('INSERT INTO Lib_user(id, name, ')
    
@bp.route('/main')
def main():
    # with sql.connect('tb_book_info.db') as con:
    #     cur =con.cursor()
    #     cur.execute('SELECT * FROM tb_book_info')
    #     result = cur.fetchall()
    #     print(result)
    return render_template('main.html')