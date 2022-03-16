import requests

# API to get all the patient
session = requests.session()
response = session.get('http://127.0.0.1:8000/patient/')
print('Get All Patient(s): ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)

# API to get a specific patient
patient_id = 1
session = requests.session()
response = session.get('http://127.0.0.1:8000/patient/' + str(patient_id))
print('Get Patient ' + str(patient_id) + ': ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)