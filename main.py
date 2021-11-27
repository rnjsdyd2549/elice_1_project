# 서버의 시작 지점 
from flask import Flask, render_template, request
import sqlite3 as sql
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config) # config 에서 가져온 파일을 사용합니다.

    db.init_app(app) 
    # SQLAlchemy 객체를 app 객체와 이어줍니다.
    Migrate().init_app(app, db)

    import main_view # view 파일 불러오는구나 !!! 
    import models
    app.register_blueprint(main_view.bp) # bp 등록시켜줘야 한다 !! 

    app.secret_key = "seeeeeeeeeeeecret"
    app.config['SESSION_TYPE'] = 'filesystem'

    return app

if __name__ == '__main__':
    create_app().run(debug=True)