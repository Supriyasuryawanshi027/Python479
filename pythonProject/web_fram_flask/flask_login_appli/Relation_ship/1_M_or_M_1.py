from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/rels'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
print("One to Many or Many to one")
class Student(db.Model):
    Sid = db.Column('Stu_id', db.Integer, primary_key=True)
    Sname = db.Column('Stu_name',db.String(30))
    Sage = db.Column('Stu_age', db.Integer())
    Semail = db.Column('Stu_email',db.String(50))
    curref=db.relationship('Course', backref='stupref', lazy=False, uselist=True)

class Course(db.Model):
    Cid = db.Column('Cu_id', db.Integer, primary_key=True)
    Cname = db.Column('Cu_name', db.String(30))
    Cfee = db.Column('Cu_fee', db.Integer())
    Stu_id = db.Column('Stud_id', db.ForeignKey('student.Stu_id'), unique=False, nullable=True)


if __name__=='__main__':
    db.create_all()

    S1 = Student(Sid=101, Sname='Supriya', Sage=25, Semail='su@gmail.com' )
    C1 = Course(Cid=100, Cname="Python", Cfee = 40000 )
    C2 = Course(Cid=200, Cname="Auto_Testing", Cfee = 20000)
    print('Using Relationship')
    db.session.add(S1)
    db.session.commit()
    db.session.add_all([C1, C2])
    db.session.commit()

    S1.curref.extend([C1,C2])
    db.session.commit()

    print('Using backref...')
    S2 = Student(Sid=102, Sname='Shiv', Sage=28, Semail='Shi@gmail.com')
    C3 = Course(Cid=300, Cname="Java", Cfee=50000)
    C4 = Course(Cid=400, Cname="Manua_Testing", Cfee=20000)
    db.session.add(S2)
    db.session.commit()

    C3.stupref = S2
    C4.stupref = S2
    db.session.add_all([C3, C4])
    db.session.commit()

    S2.curref.extend([ C3, C4])
    db.session.commit()

    print('Using FK...')
    S3 = Student(Sid=103, Sname='Suvarna', Sage=22, Semail='Suv@gmail.com')
    db.session.add(S3)
    db.session.commit()
    C5 = Course(Cid=500, Cname=".Net", Cfee=50000, Stu_id = S3.Sid)
    C6 = Course(Cid=600, Cname="PHP", Cfee=50000, Stu_id = S3.Sid)
    db.session.add_all([C5, C6])
    db.session.commit()