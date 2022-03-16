import requests

# API to get all the user
session = requests.session()
response = session.get('http://127.0.0.1:8000/user/')
print('Get All User(s): ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)

# API to get a specific user
user_id = 1
session = requests.session()
response = session.get('http://127.0.0.1:8000/user/' + str(user_id))
print('Get User ' + str(user_id) + ': ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)