from flask import Flask, render_template, flash, redirect
from flask.helpers import url_for
from flask.wrappers import Response
import requests
import json
from flask_wtf import FlaskForm
from werkzeug.datastructures import Headers
from werkzeug.wrappers import response
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired,DataRequired,Length


app = Flask(__name__)

app.config['SECRET_KEY']= "VeryVerySecret!"



reg_url = 'https://revelmyra.net/user_api/v1/account/registration/'
login_url = 'https://revelmyra.net/api/user/v1/account/login_session'
dashboard_url = 'https://revelmyra.net/dashboard'
my_headers={'Content-Type': 'application/x-www-form-urlencoded'}


############# Forms Section ####################

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length( min=3, max=250)])
    email = StringField('Email', validators=[DataRequired(), Length( min=3, max=250)])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired(), Length( min=3, max=250)])
    terms_of_service = BooleanField("I accept terms of condition", validators=[DataRequired()])
    submit = SubmitField('Sign Up') 
    def __repr__(self,username,email,password,name,terms_of_service,submit):
        return(self.username,self.email, self.password, self.name,self.terms_of_service, self.submit)       
        

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length( min=3, max=250)])
    password = PasswordField('Password', validators=[DataRequired(), Length( min=3, max=250)])
    submit = SubmitField('Login') 
    def __repr__(self,email,password,submit):
        return(self.email, self.password,  self.submit)   



############## Routes  and view section #########################


    



@app.route('/register', methods=['GET','POST'])
def register():   
    form = RegisterForm()
    data = {
        "username": form.username.data,
        "email":  form.email.data,
        "password": form.password.data,
        "name": form.name.data,
        "terms_of_service": form.terms_of_service.data,
        "submit": form.submit.data   
    }
    
   
    if form.validate_on_submit():
        requests.post(reg_url,data, allow_redirects=True)
        print(form.data)
        return redirect (dashboard_url)
           
    return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    data = {
        "email": form.email.data,
        "password": form.password.data
    }
    if form.validate_on_submit():
        if form.email.data == form.email.data and form.password.data == form.password.data:
            requests.post(login_url,form.data,my_headers, allow_redirects=True)
            
            print(requests.api)
            print(dict(form.data))
            return redirect(dashboard_url)
            
    return render_template('login.html', title='Login', form=form)

       
    



if __name__ == "__main__":
    app.run(debug=True)
