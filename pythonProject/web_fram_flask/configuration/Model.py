from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__="EMPSAMPLE"

    id = db.Column('emp_id',db.Integer,primary_key=True)
    name = db.Column('emp_name', db.String(30))
    age = db.Column('emp_age', db.Integer)
    salary = db.Column('emp_salary', db.Float)
    role = db.Column('emp_role', db.String(30))
    gender = db.Column('emp_gender', db.String(30))
    skills = db.Column('emp_skills', db.String(30))
    city = db.Column('emp_city', db.String(30))
    hobbies = db.Column('emp_hobbies', db.String(30))
db.create_all()