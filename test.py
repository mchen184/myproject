import requests 
import json

BASE = "http://127.0.0.1:5000/"

data = [{"first_name": "Joe","last_name": "Smith","userid": "jsmith","groups": "admins"},
        {"first_name": "Adam","last_name": "John","userid": "add","groups": "users"}]

for i in range(len(data)):
	response = requests.post(BASE + "users/" + data[i]['userid'],data[i])
#	print (data[i]['userid'])
	print(response.json())

# invalid get
input()
response = requests.get(BASE + "users/js")
print(response.json())
#remove a record 
input()
response = requests.delete(BASE + "users/jsmith")
print(response)
#this would return with user id add
input()
response = requests.get(BASE + "users/add")
print(response.json())
#update record
input()
response = requests.put(BASE + "users/add", {"first_name": "Adam","last_name": "John","userid": "add","groups": "owner"})
print(response.json())

