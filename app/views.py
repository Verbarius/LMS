from app import app
from flask import jsonify
from app.src.meta import Meta


@app.route("/")
@app.route("/index")
@app.route("/help")
def index():
    string_help = "Help"
    # return string_help
    return jsonify(
        meta={Meta("200", [], []).get_info()},
        data={}
    )


@app.route("/login")
def login():
    pass


@app.route("/registration")
def registration():
    pass


@app.route("/user/show_profile")
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

