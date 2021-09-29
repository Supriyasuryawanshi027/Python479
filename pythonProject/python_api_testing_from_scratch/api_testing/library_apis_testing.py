import requests

BASE_API_URI = 'http://127.0.0.1:5000/lib/api'

def check_for_api():
    response = requests.get(BASE_API_URI+'/welcome')
    print(response.text)
    #assert  response.text == 'Welcome to api testing'


def add_new_book():
    book_json = {
         "Book_id" : "Python",
         "Book_name" : 23,
         "Book_qty" : 289.23,
         "Book_price" : "Mr. Shiv"
       }
    response = requests.post(BASE_API_URI + "/", json = book_json)
    print(response.json())


if __name__ == '__main__':
    #check_for_api()
    add_new_book()




