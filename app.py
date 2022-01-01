from flask import Flask, render_template
from flask_restful import Api, Resource
import requests
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY']= "HEMMELIG"


base_url = 'https://baretest.xyz'
reg_url = base_url + '/user_api/v1/account/registration/'
login_url = base_url +'/api/user/v1/account/login_session'
dashboard_url = base_url + '/dashboard'

class MyForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    name = StringField("Name")
    #selects = SelectField('Select', choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')])
    #radios = RadioField('Radios', default='option1', choices=[('option1', 'Option1'), ('option2', 'Option2 ')])  

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = MyForm()
    if form.validate_on_submit():
        results = {
            'username' : form.username.data,
            'email' : form.email.data,
            'password' : form.password.data,
            'name' : form.name.data,
            
        }
        return render_template('results.html', **results)
    return render_template('register.html', form=form)
print(reg_url)
print(login_url)
print(dashboard_url)




if __name__ == "__main__":
    app.run(debug=True)