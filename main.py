from flask import Flask, url_for, request, render_template, redirect, make_response, session
import json
from data.job import Job
from data.user import User
from flask_login import LoginManager, login_user, logout_user, login_required

from sqlalchemy.testing.provision import drop_db

from data.LoginFrom import LoginForm
from data.RegisterForm import RegisterForm
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MASLO_3242565_ZOT93429'
login_manager = LoginManager()
login_manager.init_app(app)
param = {'header': 'Миссия колонизации марса',
         'content': 'И на марсе будут яблони цвести!'}


@app.route('/index/<title>')
def index(title):
    global param
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/list_prof/<list>')
def list_prof(list):
    global param
    list_jobs = 'инженер исследователь, пилот, врач, агроном, ученый, строитель, программист, навигатор'.split(', ')
    return render_template('jobs.html', jlist=list_jobs, type=list, **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        'title' : 'Анкета',
        'surname': 'Egorov',
        'name': 'Egor',
        'education': 'высшее',
        'profession': 'инженер',
        'sex': 'male',
        'motivation': 'мечта',
        'ready': True
    }
    return render_template('auto_answer.html', **param, **data)


@app.route('/')
def jobs():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    print(jobs)
    for i in session.query(User):
        print(i.name)
    return render_template('table.html', jobs=jobs, **param)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title="Авторизация", form=form)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            age = form.age.data,
            position=form.position.data,
            speciality=form.spec.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form, **param)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init('db/mars.db')
    app.run(port=8080, host='127.0.0.1')
