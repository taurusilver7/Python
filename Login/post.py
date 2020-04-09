#!/usr/bin/env python

import requests

target_url = "http://10.0.2.11/dvwa/login.php"
data_dict = {"username": "admin", "password": "password", "login": "submit"}

response = requests.post(target_url, data=data_dict)
print(response.content)
