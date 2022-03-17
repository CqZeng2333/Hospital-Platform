import requests

# API to get all chat(s)
session = requests.session()
response = session.get('http://127.0.0.1:8000/chat/')
print('Get All chat(s): ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)

# API to get chat(s) from a specific user
user_id = 1
session = requests.session()
response = session.get('http://127.0.0.1:8000/chat/from/' + str(user_id))
print('Get All chat(s) for User ' + str(user_id) + ': ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)

# API to get chat(s) to a specific user
user_id = 2
session = requests.session()
response = session.get('http://127.0.0.1:8000/chat/to/' + str(user_id))
print('Get All chat(s) for User ' + str(user_id) + ': ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)

# API to create new chat for a specific user
from_who = 1
to_who = 2
chat_data = {
    'from_who': from_who,
    'to_who': to_who,
    'upload_text': 'Test chat text'
}
chat_file = {
    'upload_file': ('Upload_test_file.txt', open('chat/media/Upload_test_file.txt', 'rb'))
}
session = requests.session()
response = session.post('http://127.0.0.1:8000/chat/add/', data=chat_data, files=chat_file)
print('Create New Chat from User' + str(from_who) + ' to User ' + str(to_who) + ': ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)