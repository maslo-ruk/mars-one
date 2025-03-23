from flask import Flask, url_for, request, render_template, redirect
import json
from data.job import Job
from data.user import User

from sqlalchemy.testing.provision import drop_db

from data.LoginFrom import LoginForm
from data import db_session


app = Flask(__name__)
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

@app.route('/login')
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect('/success')

@app.route('/')
def jobs():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    print(jobs)
    return render_template('table.html', jobs=jobs, **param)



if __name__ == '__main__':
    db_session.global_init('db/mars.db')
    app.run(port=8080, host='127.0.0.1')