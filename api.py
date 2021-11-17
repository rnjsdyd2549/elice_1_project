from flask import Blueprint, jsonify, render_template
bp = Blueprint('bp', __name__)

@bp.route('/')
def home_login():
    return render_template('index.html')

@bp.route('/join')
def register():
    return render_template('join.html')

@bp.route('/main', methods=["GET"])
def main():
    return render_template('main.html')