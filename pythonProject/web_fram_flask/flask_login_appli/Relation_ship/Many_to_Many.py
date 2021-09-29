from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/rels'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
print("Many to Many")

Line_item=db.Table('Line_item',
                 db.Column('S_id', db.Integer, db.ForeignKey('sales.sale_id'), unique=False),
                 db.Column('P_id', db.Integer, db.ForeignKey('product.id'), unique=False)
                )
class Sales(db.Model):

    sl_id = db.Column('sale_id', db.Integer, primary_key=True)
    sl_date=db.Column('sale_date',db.DATE)
    sl_age=db.Column('sale_quantity', db.Integer())
    sl_discount=db.Column('sale_discount',db.Integer())
    prorefs=db.relationship('Product', secondary='Line_item', backref=db.backref('selrefs',lazy=True))

class Product(db.Model):
    p_id = db.Column('id', db.Integer, primary_key=True)
    Product = db.Column('product', db.String(30))
    P_price = db.Column('price', db.Float())
    Manufacture_id = db.Column('manufacture', db.Integer())

if __name__=='__main__':
    db.create_all()
    print("Sales data add......")
    S1 = Sales(sl_id = 1, sl_date = '2021/8/8', sl_age = 28, sl_discount = 15)
    S2 = Sales(sl_id = 2, sl_date = '2021/8/16', sl_age = 25, sl_discount = 10)
    S3 = Sales(sl_id = 3, sl_date = '2021/8/28', sl_age = 32, sl_discount = 20)

    db.session.add_all([S1, S2, S3])
    db.session.commit()

    print("Product data add......")
    P1 = Product(p_id= 56, Product = 'Chocolate', P_price = 100, Manufacture_id = 1)
    P2 = Product(p_id= 87, Product = 'cloth', P_price = 2000, Manufacture_id = 2)
    P3 = Product(p_id= 34, Product = 'Mobile', P_price = 3000, Manufacture_id = 3)

    db.session.add_all([P1, P2, P3])
    db.session.commit()

    S1.prorefs.extend([P1, P3])
    S2.prorefs.extend([P2, P3])
    S3.prorefs.extend([P2, P1])
    db.session.commit()
    import sys
    sys.exit(0)








    emp5 = Emple.query.filter_by(id=555).first()
    Address=Addr.query.all()
    emp5.adrrefs.extend([Address[1],Address[3]])
    db.session.commit()
    db.session.commit()    #db.session.commit()