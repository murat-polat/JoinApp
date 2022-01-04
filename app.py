from enum import unique
from os import name
from flask import Flask, render_template, flash, redirect
from flask.helpers import url_for
from flask_restful import Api, Resource
#from flask_sqlalchemy import SQLAlchemy
import requests
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired,DataRequired,Length


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY']= "VeryVerySecret!"

######### Database section is inactive. If you want to use DB just activate it :)  ######

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

## Here the API's section (base_url) below, must be changed to your domain(LMS_HOST) ##



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(120),  nullable=False)
#     name = db.Column(db.String(20), unique=True, nullable=False)
#     terms_of_service = db.Column(db.Boolean, nullable=False)
#     def __repr__(self):
#         return f"User('{self.username}','{self.email}','{self.password}','{self.name}', '{self.terms_of_service}')" 

############# Doamin and URL section ############ 

reg_url = 'https://baretest.xyz/user_api/v1/account/registration/'
login_url = 'https://baretest.xyz/api/user/v1/account/login_session'
dashboard_url = 'https://baretest.xyz/dashboard'
my_headers={'Content-Type': 'application/x-www-form-urlencoded'}


############# Forms Section ####################

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length( min=3, max=250)])
    email = StringField('Email', validators=[DataRequired(), Length( min=3, max=250)])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired(), Length( min=3, max=250)])
    terms_of_service = BooleanField("I accept terms of condition", validators=[DataRequired()])
    submit = SubmitField('Sign Up') 
    



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length( min=3, max=250)])
    password = PasswordField('Password', validators=[DataRequired(), Length( min=3, max=250)])
    submit = SubmitField('Login') 



############## Routes  and view section #########################


     
        
@app.route('/', methods=['GET','POST'])
def index():
    form = RegisterForm()
    # if form.validate_on_submit():
    #     flash(f'Account created for {form.username.data} !', 'success')
    data = {
        "username": form.username.data,
        "email": form.email.data,
        "password": form.password.data,
        "name": form.name.data,
        "terms_of_service":form.terms_of_service.data
        }
    requests.post(reg_url,data, my_headers)
      

    return render_template('index.html',form=form)  


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    data = {
        "username": form.username.data,
        "email": form.email.data,
        "password": form.password.data,
        "name": form.name.data,
        "terms_of_service":form.terms_of_service.data
    }
    requests.post(reg_url,data, my_headers)
    if form.validate_on_submit():
        return redirect (dashboard_url, form=form)    
    return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = RegisterForm()
    data = {
        "email": form.email.data,
        "password": form.password.data
    }
    requests.post(login_url,data, my_headers)
    if form.validate_on_submit():
        return redirect (dashboard_url)
    return render_template('login.html', title='Login', form=form)

       
    



if __name__ == "__main__":
    app.run(debug=True)