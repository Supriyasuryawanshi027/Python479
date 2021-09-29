from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from configuration.Model import Employee,db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
      #http://localhost:5000

@app.route('/emp/welcome')          #http://localhost:5000/emp/welcome
def welcome_page():
    return render_template('employee.html')
    #return 'Welcome 1122 to python web application home'

def convert_multi_tostr(values):
    #values =["A","B","C"]
    finalvalues=' '
    for ind, item in enumerate(values):
        if ind==0:
            finalvalues=item
        else:
            finalvalues=finalvalues +',' +item
    return finalvalues


@app.route('/emp/add/',methods =['POST', 'GET'])
def add_new_employee():
    result =''
    data=''
    if request.method =="POST":
        formdata=request.form
        emp=Employee(id=formdata.get('eid'),
                       name=formdata.get('enm'),
                       age=formdata.get('eag'),
                       salary=formdata.get('esal'),
                       role=formdata.get('erole'),
                       gender=formdata.get('Gender'),
                       skills=convert_multi_tostr(formdata.getlist('Skills')),  # m
                       city=formdata.get('City'),
                       hobbies=convert_multi_tostr(formdata.getlist('Hobbies')))
        eid=formdata.get('eid')
        emprecord=Employee.query.filter_by(id=eid).first()
        if emprecord:
            result ="Duplicate records"
            data=emp
        else:
            db.session.add(emp)
            db.session.commit()
            result = "Data Successfully Submitted..."
            data= Employee(id=0,
                   name='',
                   age=0,
                   salary=0.0,
                   role ='',
                   gender='',
                   skills='',  # m
                   city='',
                   hobbies='')
    return render_template('employee.html', message=result,emp= data)


    '''print("From submitted")
    print('POST METHOD', request.form)
    print('GET METHOD',request.args)
    nm=request.form.get('enm')
    age = request.form.get('eag')
    skills = request.form.getlist('Skills')
    print("EMPLOYEE NAME:", nm)
    print("EMPLOYEE AGE:", age)
    print("EMPLOYEE SKILLS:", skills)'''



@app.route('/emp/update/')
def update_employee():
    pass


@app.route('/emp/search/all/')
def get_all_employees():
    return render_template('show.html', emplist=Employee.query.all())

@app.route('/emp/search/')
def search_empoyees():
    pass

@app.route('/emp/delete/')
def delete_employee():
    pass

if __name__== '__main__':
    app.run(debug=True)

