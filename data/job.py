import sqlalchemy
from .db_session import SqlAlchemyBase
import datetime
from sqlalchemy import orm


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    teamleader = orm.Relationship('User')
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished =  sqlalchemy.Column(sqlalchemy.Boolean)
