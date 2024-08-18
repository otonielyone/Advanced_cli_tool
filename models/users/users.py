from os import path 
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
            return str(self.user_id) 

    def __repr__(self):
        return '<User {}>'.format(self.username)


def create_database(app):
    if not path.exists('templates/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


