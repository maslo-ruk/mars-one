from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    userid = StringField('Логин', validators=[DataRequired()])
    userpassword = StringField('Логин', validators=[DataRequired()])
    captainid = StringField('Логин', validators=[DataRequired()])
    captainpassword = StringField('Логин', validators=[DataRequired()])
    submit = SubmitField('Войти')