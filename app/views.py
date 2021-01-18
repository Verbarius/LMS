from app import app, db
from flask import jsonify, request, g, make_response, Blueprint
from app.src.answer import Answer
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import app.utils as utils
from flask_login import LoginManager

from .models import User


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


@app.route('/', methods=["GET", "POST"])
def index():
    return make_response(jsonify(Answer(200, "", []).get_info()))


@app.route('/login', methods=["POST"])
def login():
    email = request.json["login"]
    user = User.query.filter_by(email=email).first()
    password = request.json["pass"]

    if not check_password_hash(user.password, password):
        return make_response(jsonify(Answer(401, "Неверный логин или пароль!", []).get_info()))

    login_user(user)
    return make_response(jsonify(Answer(200, "", []).get_info()))


@app.route("/registration", methods=["POST"])
def registration():
    email = request.json["email"]
    code = request.json["code"]
    password = request.json["pass"]

    user = User.query.filter_by(code=code).first()

    if user is None:
        return make_response(jsonify(Answer(401, "Такого пользователя не существует!", []).get_info()))

    if not utils.valid_password(password):
        return make_response(jsonify(Answer(401, "Пароль слишком простой", []).get_info()))

    user.email = email
    user.password = generate_password_hash(password, method='sha256')
    db.session.commit()
    return make_response(jsonify(Answer(200, "", []).get_info()))


@app.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return make_response(jsonify(Answer(200, "", []).get_info()))


@app.route('/show', methods=["POST"])
@login_required
def show_info():
    return make_response(jsonify(Answer(200, "", utils.get_user_info(current_user))))


@app.route('/show_all', methods=["POST"])
@login_required
def show_info():
    return make_response(jsonify(Answer(200, "", utils.get_all_user_info(current_user))))


# @app.error_handler(401)
# def unauthorized():
#     return jsonify(Answer(401, "Unauthorized access", []).get_info())


# @app.route("/login", methods=["POST"])
# def login():
#     user = User.query.filter_by(email=request.json["login"]).first()
#     if user is None or user.password != request.json["pass"]:
#         g.auth = True
#         return make_response(jsonify(Answer(400, "Не верный логин или пароль!", [])))
#     else:
#         return make_response(jsonify(Answer(200, "", [])))   # TODO: расставить правильные ошибки


# @app.route("/user/show_profile")
# @login_required
# def show_profile():
#     pass
#
#
# @app.route("/user/edit_profile")
# def edit_profile():
#     pass
#
#
# @app.route("/students/show_profile")
# def info_profile():
#     pass
#
#
# @app.route("/students/get_students")
# def get_students():
#     pass
#
#
# @app.route("/user/get_courses")
# def get_courses():
#     pass
#
#
# @app.route("/user/get_course")
# def get_course():
#     pass

