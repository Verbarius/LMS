from app import db

# constants start

# constants end


# models start
class User(db.Model):
    __tablename__ = "user"  # optional

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)  # зачем index - не помню
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
