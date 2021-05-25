import requests 
import json

BASE = "http://127.0.0.1:5000/"

data = [{"first_name": "Joe","last_name": "Smith","userid": "jsmith","groups": "admins"},
        {"first_name": "Adam","last_name": "John","userid": "add","groups": "users"}]

for i in range(len(data)):
	response = requests.post(BASE + "groups/" + data[i]['groups'],data[i])
#	print (data[i]['userid'])
	print(response.json())