from flask import Blueprint, jsonify, render_template, request, flash, redirect
from flask_bcrypt import Bcrypt
from db_connect import db
from email_validator import validate_email, EmailNotValidError
from flask_login import login_required, login_user, current_user, logout_user
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

from models import Lib_User, Book, Rent_user, Book_comment
bp = Blueprint('bp', __name__)
bcrypt = Bcrypt()
# @login_manager.user_loader
# def load_user(email):
#     return Lib_User.query.filter_by(email=email).first()

@bp.route('/')
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email:
            flash('Email을 입력해주세요.')
            return render_template('index.html')
        else:
            try:
                validate_email(email)
            except EmailNotValidError:
                flash('Email 형식이 아닙니다.')
                return render_template('index.html')

        if not password:
            flash('패스워드를 입력해주세요.')
            return render_template('index.html')

        user = Lib_User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('패스워드가 틀렸습니다.')
        else:
            login_user(user)
            return redirect('/')

    return render_template('index.html')

@bp.route('/join', methods=["GET", "POST"])
# 회원가입 !
def join():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not email:
            flash('Email을 입력해주세요.')
            return render_template('join.html')
        else:
            try:
                validate_email(email)
            except EmailNotValidError:
                flash('Email 형식이 아닙니다.')
                return render_template('join.html')

        if not name:
            flash('Name을 입력해주세요.')
            return render_template('join.html')

        if not password1 or not password2:
            flash('패스워드를 입력해주세요.')
            return render_template('join.html')

        if password1 != password2:
            flash('password가 일치하지 않습니다.')
            return render_template('join.html')

        if len(password1) < 8:
            flash('password는 8자 이상이여야합니다.')
            return render_template('join.html')

        if not any(char.isdigit() for char in password1):
            flash('숫자가 포함되어야합니다.')
            return render_template('join.html')
        special_char = '`~!@#$%^&*()_+|\\}{[]":;\'?><,./'
        if not any(char in special_char for char in password1):
            flash('특수문자가 포함되어야합니다.')
            return render_template('join.html')

        user = Lib_User.query.filter_by(email=email).first()
        if user:
            flash('이미 존재하는 유저입니다.')
            return render_template('signup.html')

        new_user = Lib_User(email=email, name=name,
                        password=generate_password_hash(password1, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect('/join')

    return render_template('join.html')

# @bp.route('/join', methods=['POST'])
# def adduser():
#     user_name = request.form.get('userName')
#     user_id = request.form.get('userId')
#     user_pw = request.form.get('userPw')

#     user = Lib_User(user_name, user_id, user_pw)
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({"result": "success"})
    
@bp.route('/main')
def main():
    books = Book.query.all()
    if request.method == 'POST':
        book_id = request.form.get('book_id')
        if not book_id:
            flash('book_id는 필수 파라미터 입니다.')
            return render_template('index.html', books=books)
        try:
            book_id = int(book_id)
        except ValueError:
            flash('book_id는 정수여야 합니다.')
            return render_template('index.html', books=books)

        book = Book.query.filter_by(id=book_id).first()
        if book is None:
            flash('대출하려는 책을 찾을 수 없습니다.')
            return render_template('index.html', books=books)

        if book.stock == 0:
            flash('모든 책이 대출중입니다')
        else:
            rent = Rent_user(book_id=book_id, user_id=current_user.id, rent_at=date.today())
            db.session.add(rent)
            book.stock -= 1
            db.session.commit()
            flash(f'{book.name}을 대여했습니다.')
        return redirect('/main')

    return render_template('main.html', books=books)
