from api_generation.config import *

class Book(db.Model):
    id = db.Column("Book_id", db.Integer, primary_key=True)
    name = db.Column("Book_name", db.String (30))
    qty = db.Column("Book_qty", db.Integer)
    price = db.Column("Book_price", db.Float)
    authors = db.relationship("Author", lazy = True, backref="book")

class Author(db.Model):
    id = db.Column("Author_id", db.Integer, primary_key=True)
    name = db.Column("Author_name", db.String(50))
    bookid = db.Column("Book_id", db.ForeignKey("book.Book_id"), unique =False, nullable = True)

db.create_all()
