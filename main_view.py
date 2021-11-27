from os import name
from flask import Blueprint, render_template, request, url_for, session, redirect
from flask.helpers import flash
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
# 폴더.파일 명

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home():
    book_list = book_info.query.order_by(book_info.id.asc())
    print(book_list)
    return render_template('main.html', book_list=book_list)

@bp.route('/main')
def main():
    book_list = book_info.query.order_by(book_info.id.asc())
    return render_template('main.html', book_list=book_list)


# 
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        # 회원가입 과정을 거쳐야겠다 .!! 
        # 만약에 같은 아이디면 ... ?! 
        user = LibUser.query.filter_by(user_email=request.form['user_email']).first()
        if not user:
            # 회원가입진행
            password = generate_password_hash(request.form['password'])

            user = LibUser(name=request.form['name'], user_email=request.form['user_email'], password=request.form['password'])

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('main.home')) # 사이트 들어가면 주소 다시 작성해주는것이 redirect, 그걸 url_for 로 자동으로 바꿔서 보내주는것 
        else:
            return "이미 가입된 아이디입니다"

# 잘못된 데이터가 들어갈 경우
# 복구가 안되니, 실제 디비에 반영 안하고 미리보기만. 실제 저장은 커밋해야함 ..!! 

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        id       = request.form.get('user_email')
        password    = request.form['password']

        user_data = LibUser.query.filter_by(user_email=id).first()

        if not user_data:
            return "없는 아이디입니다."
        elif password != user_data.password:
            return "비밀번호가 틀립니다."
        else:
            session.clear()
            session['user_email'] = id
            session['name'] = user_data.name
            # 세션 덕분에 로그안시 제일 밑에 누구누구 님 안녕하세요 뜨는거임 ! 
            return redirect(url_for('main.home'))

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

@bp.route('/rent')
def rent():
    return '대여목록들을 보여주세요'

@bp.route('/return')
def book_return():
    return '책 반랍가능하게 해주세요.'

@bp.route("/books/<int:book_id>", methods=['GET', 'POST'])
def book_detail(book_id):
    book = book_info.query.filter_by(id=book_id).first()
    if book is None:
        flash("책을 찾을 수 없습니다.")
        return redirect('/')
    
    return 'hhh'