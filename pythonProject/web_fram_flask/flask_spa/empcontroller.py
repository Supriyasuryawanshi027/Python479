import bdb

from config import *
from flask import Flask,request,render_template
from models import Employee

def validate_form_data(formdata):
    age = formdata.get('age')
    if not age or not age.isnumeric() or int(age)<=0:
        return "Invalid Age Entered "



@app.route("/index")
def welcome_page():
    return render_template('Employee.html',emp = Employee.dummy_employee_instance(), emplist=Employee.query.all())

def convert_multi_tostr(values):
    #values =["A","B","C"]
    finalvalues=' '
    for ind, item in enumerate(values):
        if ind==0:
            finalvalues=item
        else:
            finalvalues=finalvalues +',' +item
    return finalvalues



@app.route("/emp/persist", methods=['POST','GET'])
def save_or_update_emp():
    message=''
    if request.method=='POST':
        formdata=request.form
        eid=formdata.get('eid')
        dbemp=Employee.query.filter_by(id=eid).first()
        empformdata=Employee(firstname=formdata.get('firstname'),
                       lastname = formdata.get('lastname'),
                        gender = formdata.get('gender'),
                        roles = formdata.get('roles'),
                        age = formdata.get('age'),
                        email = formdata.get('email'),
                        salary = formdata.get('salary'),
                        contact = formdata.get('contact'),
                        Address= formdata.get('Address'),
                        Skills = convert_multi_tostr(formdata.getlist('Skills')),
                        domain=convert_multi_tostr(formdata.getlist('project')))
        error=validate_form_data(formdata)
        if error:
            return render_template('Employee.html',
                                   emp=empformdata,
                                   ageerror = error)
        if dbemp:
            dbemp.firstname=formdata.get('firstname')
            dbemp.lastname = formdata.get('lastname')
            dbemp.gender = formdata.get('gender')
            dbemp.roles = formdata.get('roles')
            dbemp.age = formdata.get('age')
            dbemp.email = formdata.get('email')
            dbemp.salary = formdata.get('salary')
            dbemp.contact = formdata.get('contact')
            dbemp.Address = formdata.get('Address')
            dbemp.Skills = convert_multi_tostr(formdata.getlist('Skills'))
            dbemp.domain = convert_multi_tostr(formdata.getlist('project'))
            db.session.commit()
            result="Employee record Updated....."
        else:
            emp=empformdata
            db.session.add(emp)
            db.session.commit()
            result = "Employee record added....."
    return render_template('Employee.html',
                           emp=Employee.dummy_employee_instance(),
                           message=result,
                           emplist=Employee.query.all())

@app.route("/edit/<int:eid>")
def edit_employee(eid):
    dbemp = Employee.query.filter_by(id=eid).first()
    return render_template('employee.html',
                           emp=dbemp,
                            emplist=Employee.query.all())


@app.route("/delete/<int:eid>")
def delete_employee(eid):
    dbemp = Employee.query.filter_by(id=eid).first()
    if dbemp:
        db.session.delete(dbemp)
        db.session.commit()

    return render_template('employee.html',
                           emp=Employee.dummy_employee_instance(),
                           result="",
                           emplist=Employee.query.all())



if __name__=='__main__':
    app.run(debug=True)