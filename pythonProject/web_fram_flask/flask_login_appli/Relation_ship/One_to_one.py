from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/rels'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

print("One to One")
class People(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name=db.Column('emp_name',db.String(30))
    age=db.Column('emp_age', db.Integer())
    driref=db.relationship('DrivL', backref='peoref', lazy=False, uselist=False)

class DrivL(db.Model):
    Lno = db.Column('Lno', db.Integer, primary_key=True)
    city = db.Column('city', db.String(30))
    UserId = db.Column('P_id', db.ForeignKey('people.id'), unique=True, nullable=True)

if __name__=='__main__':
    db.create_all()
    p1 = People.query.filter_by(id=111).first()
    p2 = People.query.filter_by(id=222).first()

    print(p1.__dict__)
    print(p2.driref.__dict__)

    import sys
    sys.exit(0)

    print("People Table Created Succesfully...")
    p1=People(id=111, name='AAA', age=25)
    p2 = People(id=222, name='BBB', age=26)
    p3 = People(id=333, name='CCC', age=27)
    p4 = People(id=444, name='DDD', age=28)
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()



    print("DrivL Table Created Succesfully...")
    L1=DrivL(Lno=145, city='Janapur',UserId=p1.id)
    L2 = DrivL(Lno=246, city='B.Kalyan', UserId=p2.id)
    L3 = DrivL(Lno=347, city='Bidar', UserId=p3.id)
    L4 = DrivL(Lno=448, city='Karnataka', UserId=p4.id)
    db.session.add_all([L1, L2, L3, L4])
    db.session.commit()