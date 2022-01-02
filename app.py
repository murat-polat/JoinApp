from flask import Flask, render_template
from flask_restful import Api, Resource
import requests
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired,DataRequired


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY']= "VeryVerySecret!"

## Here the API's section (base_url) below, must be changed to your domain(LMS_HOST) ##
base_url = 'https://baretest.xyz'
reg_url = base_url + '/user_api/v1/account/registration/'
login_url = base_url +'/api/user/v1/account/login_session'
dashboard_url = base_url + '/dashboard'

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    terms_of_service = BooleanField("I accept terms of condition", validators=[DataRequired()])
    submit = SubmitField('Sign Up') 


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login') 



@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)




@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    
    # username = form['username']
    # email = form['email']
    # password = form['password']
    # name = form['name']

        
    return render_template('register.html', title='Register', form=form)





if __name__ == "__main__":
    app.run(debug=True)