from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(255),nullable=False, unique=True)
    username = db.Column(db.String(120),nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(120),nullable=False, unique=True)
    create_date = db.Column(db.DateTime , index=True,default=datetime.utcnow)
    group = db.Column(db.String(20),index=True)
    lecture = db.relationship('Lecture', backref='user', uselist=False, lazy='dynamic')
    tutor = db.relationship('Tutor', backref='user', uselist=False, lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Lecture(db.Model):
    employee_number = db.Column(db.String(10),primary_key=True)
    office_number = db.Column(db.String(10),nullable=False,unique=True)
    telephone_number = db.Column(db.String(12),nullable=False,unique=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f'User {self.employee_number}'

class Tutor(db.Model):
    student_number = db.Column(db.String(10), primary_key=True)
    account_type = db.Column(db.String(60), nullable=False)
    account_number = db.Column(db.String(60), nullable=False, unique=True)
    bank_name = db.Column(db.String(60), nullable=False)
    branch_code = db.Column(db.String(20), nullable=False)
    year_of_study = db.Column(db.String(2), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False, unique=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f'User {self.student_number}'

