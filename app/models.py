from app import db

# constants start

# constants end


# models start
class User(db.Model):
    __tablename__ = "user"  # optional

    user_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), unique=True)
    user_role = db.Column(db.String(64))
    email = db.Column(db.Text())
    password = db.Column(db.String(64))
    First_name = db.Column(db.String(64))
    Surname = db.Column(db.String(64))
    Middle_name = db.Column(db.String(64))
    telephone = db.Column(db.String(64))
    city = db.Column(db.String(64))
    information = db.Column(db.Text())
    vk = db.Column(db.Text())
    facebook = db.Column(db.Text())
    linkedIn = db.Column(db.Text())
    instagram = db.Column(db.Text())


class Student(db.Model):
    __tablename__ = "student"  # optional

    user_id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, primary_key=True)
    year_of_entry = db.Column(db.Integer)
    basis_of_education = db.Column(db.String(64))


class Course(db.Model):
    __tablename__ = "course"  # optional

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.Text())
    course_description = db.Column(db.Text())


class Course_material(db.Model):
    __tablename__ = "course_material"  # optional

    course_id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.Integer, primary_key=True)
    material_name = db.Column(db.Text())
    content = db.Column(db.Text())
    add_date = db.Column(db.DateTime())


class Group(db.Model):
    __tablename__ = "group"  # optional

    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(64))
    faculty_name = db.Column(db.String(64))
    course_num = db.Column(db.Integer)
    year_of_formation = db.Column(db.Integer)
    degree = db.Column(db.String(64))
    form_of_education = db.Column(db.String(64))


class Group_x_course(db.Model):
    __tablename__ = "group_x_course"  # optional

    group_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, primary_key=True)


class Homework(db.Model):
    __tablename__ = "homework"  # optional

    hw_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, primary_key=True)
    hw_name = db.Column(db.Text())
    hw_description = db.Column(db.Text())
    time_start = db.Column(db.DateTime())
    time_end = db.Column(db.DateTime())


class Student_x_hw(db.Model):
    __tablename__ = "student_x_hw"  # optional

    user_id = db.Column(db.Integer, primary_key=True)
    hw_id = db.Column(db.Integer, primary_key=True)
    solution = db.Column(db.Text())
    time_send = db.Column(db.DateTime())


class User_x_course(db.Model):
    __tablename__ = "user_x_course"  # optional

    user_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, primary_key=True)
    course_role = db.Column(db.String(64))
