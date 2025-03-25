from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    title = StringField('Job title', validators=[DataRequired()])
    lead_id = IntegerField('Team leader ID', validators=[DataRequired()])
    work_size = StringField('Name', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Войти')