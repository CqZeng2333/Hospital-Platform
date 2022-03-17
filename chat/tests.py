#from django.test import TestCase

# Create your tests here.
import pytest
import requests

def test_success_get_chat_from_user():
    user_id = 1
    session = requests.session()
    response = session.get('http://127.0.0.1:8000/chat/from/' + str(user_id))
    assert response.status_code == 200

def test_success_get_chat_to_user():
    user_id = 2
    session = requests.session()
    response = session.get('http://127.0.0.1:8000/chat/to/' + str(user_id))
    assert response.status_code == 200

def test_get_chat_user_not_exist():
    user_id = 5
    session = requests.session()
    response = session.get('http://127.0.0.1:8000/chat/from/' + str(user_id))
    assert response.status_code == 400

def test_get_chat_not_exist():
    user_id = 3
    session = requests.session()
    response = session.get('http://127.0.0.1:8000/chat/from/' + str(user_id))
    assert response.status_code == 404

# def test_create_chat_success():
#     chat_data = {
#         "from_who": 1,
#         "to_who": 2,
#         "upload_text": 'Test chat text',
#         "upload_file": file
#     }
#     chat_file = {
#         'upload_file': ('Upload_test_file.txt', open('chat/media/Upload_test_file.txt', 'rb'))
#     }
#     session = requests.session()
#     response = session.post('http://127.0.0.1:8000/chat/add/', data=chat_data, files=chat_file)
#     assert response.status_code == 201

def test_create_user_not_exist_measurement():
    file = open('chat/media/Upload_test_file.txt')
    chat_data = {
        "from_who": 5,
        "to_who": 5,
        "upload_text": 'Test chat text',
        "upload_file": file
    }
    chat_file = {
        'upload_file': ('Upload_test_file.txt', open('chat/media/Upload_test_file.txt', 'rb'))
    }
    session = requests.session()
    response = session.post('http://127.0.0.1:8000/chat/add/', data=chat_data, files=chat_file)
    assert response.status_code == 400

if __name__ == '__main__':
    pytest.main(['chat/tests.py', '-s'])