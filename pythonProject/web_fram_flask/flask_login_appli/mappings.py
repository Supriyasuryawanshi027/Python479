from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskdb_m'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
print("Many to Many")

emp_adr=db.Table('emp_adr',
                 db.Column('eid', db.Integer, db.ForeignKey('emple.emp_id'), unique=False),
                 db.Column('aid', db.Integer, db.ForeignKey('addr.id'), unique=False)
                )

class Emple(db.Model):

    id = db.Column('emp_id', db.Integer, primary_key=True)
    name=db.Column('emp_name',db.String(30))
    age=db.Column('emp_age', db.Integer())
    email=db.Column('emp_email',db.String(50))
    adrrefs=db.relationship('Addr', secondary='emp_adr', backref=db.backref('emprefs',lazy=True))

class Addr(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    city = db.Column('city', db.String(30))




if __name__=='__main__':
    emp5 = Emple.query.filter_by(id=555).first()
    Address=Addr.query.all()
    emp5.adrrefs.extend([Address[1],Address[3]])
    db.session.commit()

    import sys
    sys.exit(0)

    db.create_all()
    emp1 = Emple(id=111, name='AAA', age=25, email='aaa@gmail.com')
    emp2 = Emple(id=222, name='BBB', age=26, email='bbb@gmail.com')
    emp3 = Emple(id=333, name='CCC', age=27, email='ccc@gmail.com')
    emp4 = Emple(id=444, name='DDD', age=28, email='ddd@gmail.com')
    #db.session.add_all([emp1, emp2, emp3, emp4])
    emp5 = Emple(id=555, name='EEE', age=27, email='eee@gmail.com')
    #db.session.add(emp5)
    #db.session.commit()

    ad1 = Addr(id=1, city='Janapur')
    ad2 = Addr(id=2, city='B.Kalyan')
    ad3 = Addr(id=3, city='Bidar')
    ad4 = Addr(id=4, city='Karnataka')
    #db.session.add_all([ad1, ad2, ad3, ad4])
    ad5 = Addr(id=5, city='Bhalki')
    #db.session.add(ad5)
    #db.session.commit()


    emp1.adrrefs.extend([ad1, ad3,])
    emp2.adrrefs.extend([ad4, ad2])
    emp3.adrrefs.extend([ad2, ad4])
    emp4.adrrefs.extend([ad2, ad3])
    emp5.adrrefs.extend([ad5])


    #db.session.commit()






import sys
sys.exit(0)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskdb_m'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
print("One to Many or Many to one")
class Employ(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name=db.Column('emp_name',db.String(30))
    age=db.Column('emp_age', db.Integer())
    email=db.Column('emp_email',db.String(50))
    adrref=db.relationship('Addre', backref='empref', lazy=False, uselist=True)

class Addre(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    city = db.Column('city', db.String(30))
    empid = db.Column('eid', db.ForeignKey('employ.id'), unique=False, nullable=True)


if __name__=='__main__':
    db.create_all()

    em1=Employ(id=101, name='abc', age=41, email='abc@gmail.com' )
    ad1 = Addre(id=100, city="Pune")
    ad2 = Addre(id=200, city="HYD")
    print('Using Relationship')
    db.session.add(em1)
    db.session.commit()
    db.session.add_all([ad1, ad2])
    db.session.commit()

    em1.adrref.extend([ad1, ad2])
    db.session.commit()

    print('Using backref...')
    em2 = Employ(id=102, name='def', age=43, email='def@gmail.com')
    db.session.add(em2)
    db.session.commit()

    ad3 = Addre(id=300, city="Bidar")
    ad4 = Addre(id=400, city="B.Kalyan")
    ad3.emref=em2
    ad4.emref=em2
    db.session.add_all([ad1, ad2])
    db.session.commit()

    em2.adrref.extend([ad3, ad4])
    db.session.commit()

    print('Using FK...')
    em3 = Employ(id=103, name='ghi', age=45, email='ghi@gmail.com')
    db.session.add(em3)
    db.session.commit()
    ad5 = Addre(id=500, city="gug", empid=em3.id)
    ad6 = Addre(id=600, city="gug", empid=em3.id)
    db.session.add_all([ad5, ad6])
    db.session.commit()
import sys
sys.exit(0)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskdb_m'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

print("One to One")
class Employee(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name=db.Column('emp_name',db.String(30))
    age=db.Column('emp_age', db.Integer())
    email=db.Column('emp_email',db.String(50))
    adrref=db.relationship('Address', backref='empref', lazy=False, uselist=False)

class Address(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    city = db.Column('city', db.String(30))
    empid = db.Column('eid', db.ForeignKey('employee.id'), unique=True, nullable=True)

if __name__=='__main__':
    db.create_all()
    emp1 = Employee.query.filter_by(id=111).first()
    print(emp1.__dict__)
    print(emp1.adrref.__dict__)

    import sys
    sys.exit(0)

    ad1=Address.query.filter_by(id=1).first()
    print(ad1.__dict__)
    #print(ad1.adrref)

    import sys
    sys.exit(0)
    emp1=Employee(id=111, name='AAA', age=25, email='aaa@gmail.com')
    emp2 = Employee(id=222, name='BBB', age=26, email='bbb@gmail.com')
    emp3 = Employee(id=333, name='CCC', age=27, email='ccc@gmail.com')
    emp4 = Employee(id=444, name='DDD', age=28, email='ddd@gmail.com')
    db.session.add_all([emp1, emp2, emp3, emp4])
    db.session.commit()

    ad1=Address(id=1, city='Janapur',empid=emp1.id)
    ad2 = Address(id=2, city='B.Kalyan', empid=emp2.id)
    ad3 = Address(id=3, city='Bidar', empid=emp3.id)
    ad4 = Address(id=4, city='Karnataka', empid=emp4.id)
    db.session.add_all([ad1, ad2, ad3, ad4])
    db.session.commit()

