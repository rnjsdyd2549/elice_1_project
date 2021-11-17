from flask import Flask,render_template,jsonify,request, redirect
import pymysql
from api import bp
# SQLAlchemy 객체를 가져오세요.
from db_connect import db

app = Flask(__name__)
app.register_blueprint(bp)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ajtnlaka3!@127.0.0.1:5000/Library"

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)