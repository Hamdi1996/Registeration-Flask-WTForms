from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """ User model """

    __tablename__ = "usr"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email= db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)



class Result(db.Model):
    """result"""
    __tablename__="result"

    id = db.Column(db.Integer, primary_key=True)
    result= db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usr.id'))
    notNegative =db.Column(db.String(25))
    notPositive =db.Column(db.String(25))
    naturalWords =db.Column(db.String(25))
    commonTf=db.Column(db.String(250))
    commonIdf=db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, index=True)
    data = db.Column(db.LargeBinary)
    usr=db.relationship(User)
    header=db.Column(db.String)
    separtor=db.column(db.String(20))
