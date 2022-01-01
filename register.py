import requests
import json

url = 'https://baretest.xyz/user_api/v1/account/registration/'

data = {
    "username": "",
    "email": "",
    "password": "",
    "name": "",
    "terms_of_service": True
}
 
response = requests.post(url,data, headers={"Content-Type": "application/x-www-form-urlencoded"})
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())