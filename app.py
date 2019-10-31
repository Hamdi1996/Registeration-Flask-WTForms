import os
import time
from flask import Flask,render_template,redirect ,url_for,request
from flask_login import LoginManager, login_user, current_user, logout_user
from wtform_fields import *
from flask_sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)
app.secret_key = 'super_secret_key'
#config database

app.config['SQLALCHEMY_DATABASE_URI']='postgres://vbwlqsoyrcxozr:0e384703ae43404caf6fe1abc35a802af5c58d5ff96ad2eb8a80884020a4fe3d@ec2-54-243-44-102.compute-1.amazonaws.com:5432/d2q3b7m6b3cstj'
db=SQLAlchemy(app)

@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('home'))


    return render_template('login.html', form=login_form)


@app.route('/register',methods=['GET','POST'])
def index():
    reg_form=RegistrationForm()

    if reg_form.validate_on_submit():
        username =reg_form.username.data
        email =reg_form.email.data
        password =reg_form.password.data


        #chcek email existance

        user=User.query.filter_by(email=email).first()
        if user:
            return "Some one else has this Email !"
        #chcek email existance
        user=User.query.filter_by(username=username).first()
        if user:
            return "Some one else has this username !"

        user=User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("index.html",form=reg_form)



@app.route('/home')
def home():
    return render_template('placeholder.home.html')


@app.route('/about')
def about():
    return render_template('placeholder.dashboard.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == "POST":
        fdata =request.form["inputfile"]
        header =request.form["checkbox"]
        lTerminator=request.form["select"]

        return header+fdata+lTerminator



    return render_template('csvfile.html')



if __name__ == '__main__':
    debug=True
    app.run(host='0.0.0.0', port=5000)
