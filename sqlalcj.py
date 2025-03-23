from data.job import Job
from data.user import User
from data import db_session


db_session.global_init('db/mars.db')
user = User()
user.name = "Ridley"
user.surname = "Scott"
user.age = 21
user.position = 'captain'
user.speciality = "research engineer"
user.email = "scott_chief@mars.org"
user.address = 'module_1'
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()