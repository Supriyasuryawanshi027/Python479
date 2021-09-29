from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql//root:root@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/web/welcome')          #http://localhost:5000/webapp/welcome                       http://127.0.0.1
def welcome_page():
    return 'Welcome 112 to python web application home'      # processing on same machine





if __name__ == '__main__':
    #ans = welcome_page()
    #print(ans)
    app.run()