from flask import Flask, render_template
from flask_restful import Api, Resource
import requests
import json

app = Flask(__name__)
api = Api(app)



base_url = 'https://baretest.xyz'
reg_url = base_url + '/user_api/v1/account/registration/'
login_url = base_url +'/api/user/v1/account/login_session'
dashboard_url = base_url + '/dashboard'

   

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')
    
#@app.route('/register', method=['GET','POST'])
print(reg_url)
print(login_url)
print(dashboard_url)




if __name__ == "__main__":
    app.run(debug=True)