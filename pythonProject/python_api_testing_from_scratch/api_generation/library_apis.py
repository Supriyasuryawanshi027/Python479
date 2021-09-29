from api_generation.config import app
from flask import request
from api_generation.modul import *
import json

@app.route('/lib/api/welcome', methods=['GET'])
def welcome_api():
    return "Welcome to api testing"

@app.route('/lib/api/', methods=['POST'])
def add_new_book():
    reqbody = request.get_json()
    try:
        if reqbody:
            bkname = reqbody.get('BOOK_NAME')
            bkprice = reqbody.get('BOOK_PRICE')
            bkqty = reqbody.get('BOOK_QTY')
            bkauthor = reqbody.get('BOOK_AUTHOR')

            book = Book(name = bkname, price = bkprice, qty =  bkqty)
            db.session.add(book)
            db.session.commit()

            author = Author(Author_name = bkauthor, bookid = book.id)
            db.session.add(author)
            db.session.commit()
            return json.dumps({"SUCCESS" : " BOOK RECORD CREATED...."})
    except BaseException as e:
        return json.dumps({"FAILED" : e.args})


@app.route('/lib/api/<int:bkid>', methods=['GET'])
def search_book(bkid):
    pass


@app.route('/lib/api/<author_name>', methods=['GET'])
def search_by_author_name():
    pass


@app.route('/lib/api/<int:bid>', methods=['DELETE'])
def delete_book(bid):
    pass

@app.route('/lib/api/<int:bid>', methods=['PUT'])
def update_book(bid):
    pass


@app.route('/lib/api/', methods=['GET'])
def get_all_books():
    pass

if __name__ == '__main__':
    app.run(debug=True)

