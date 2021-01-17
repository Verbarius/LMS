from app import app
from flask import jsonify, request, g, make_response
from app.src.answer import Answer
from flask_login import login_user, logout_user, login_required
from flask_login import LoginManager
from werkzeug.exceptions import HTTPException

from .models import User


login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/login')
def login():
    email = request.json["login"]
    user = User.query.filter_by(email=email).first()
    return make_response(jsonify(Answer(200, "", [])))


@app.route('/signup')
def signup():
    return 'Signup'


@app.route("/registration")
def registration():
    pass


@app.route('/logout')
def logout():
    logout_user()
    return make_response(jsonify(Answer(200, "", []).get_info()))


@app.error_handler(401)
def unauthorized():
    return jsonify(Answer(401, "Unauthorized access", []).get_info())


@app.route('/')
@app.login_required
def index():
    return "Hello, {}!".format(app.current_user())


@app.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(email=request.json["login"]).first()
    if user is None or user.password != request.json["pass"]:
        g.auth = True
        return make_response(jsonify(Answer(400, "Не верный логин или пароль!", [])))
    else:
        return make_response(jsonify(Answer(200, "", [])))   # TODO: расставить правильные ошибки


@app.route("/registration")
def registration():
    pass


@app.route("/user/show_profile")
@login_required
def show_profile():
    pass


@app.route("/user/edit_profile")
def edit_profile():
    pass


@app.route("/students/show_profile")
def info_profile():
    pass


@app.route("/students/get_students")
def get_students():
    pass


@app.route("/user/get_courses")
def get_courses():
    pass


@app.route("/user/get_course")
def get_course():
    pass

