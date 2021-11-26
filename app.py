from flask import Flask,render_template,jsonify,request, redirect
# from flask_login import LoginManger
import pymysql
from api import bp
from db_connect import db
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.register_blueprint(bp)

# login_manager = LoginManger()
# login_manager.init_app(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://@127.0.0.1/project_L"
app.secret_key = 'secret!key!'

db.init_app(app)
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    app.run(debug=True, port=3306)

    