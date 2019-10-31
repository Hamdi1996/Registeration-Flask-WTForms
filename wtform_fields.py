#!/usr/bin/python3
# -*- coding: utf8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField
from models import *


def invalid_credentials(form ,field ):
    """Email & password checker"""
    email_entered =form.email.data
    password_entered=field.data
    user = User.query.filter_by(email=email_entered).first()
    if user is None:
        raise ValidationError("البريد الالكتروني او الاسم غير صحيح")
    elif password_entered !=user.password:
        raise ValidationError("البريد الالكتروني او الاسم غير صحيح")




class RegistrationForm(FlaskForm):
    """ Registration form"""

    username = StringField('username_label', validators=[InputRequired(message="الاسم مطلوب"), Length(min=4, max=25, message="الاسم يجب الا يقل عن 4 احرف")])
    email = EmailField('email_label', validators=[InputRequired(message="البريد الالكتروني مطلوب"), Length(max=25, message="البريد الالكتروني يجب الا يزيد عن 25 حرف")])
    password = PasswordField('password_label', validators=[InputRequired(message="مطلوب كلمه السر "), Length(min=8, max=25, message="كلمه السر يجب الا تقل عن 8 احرف")])
    confirm_pswd = PasswordField('confirm_pswd_label', validators=[InputRequired(message="تاكيد كلمه السر"), EqualTo('password', message="كلمه السر غير مطابقه")])
    submit_button =SubmitField('Create')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("البريد الالكتروني موجود بالفعل")
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("الاسم ماخوذ ,اختر اسما اخر")


class LoginForm(FlaskForm):
    """Login Form"""
    email =EmailField('email_label',validators=[InputRequired(message="البريد الالكتروني مطلوب")])
    password =PasswordField('password_label',validators=[InputRequired(message='كلمه السر مطلوب'),invalid_credentials])
    submit_button = SubmitField('Login')
