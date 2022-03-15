import requests

# API to get all the patient
session = requests.session()
response = session.get('http://127.0.0.1:8000/device/patient/')
print('Get All Patient(s): ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)

# API to get measurement(s) for a specific patient
patient_id = 1
session = requests.session()
response = session.get('http://127.0.0.1:8000/device/patient-id/' + str(patient_id))
print('Get All Measurement(s) for Patient ' + str(patient_id) + ': ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)

# API to create new measurement for a specific patient
patient_id = 1
mea_data = {
    "patient_id": 1,
    "temperature": 36.9,
    "systolic_blood_pressure": 101.0,
    "diastolic_blood_pressure": 78.0,
    "pulse": 80.0,
    "oximeter": 96.0,
    "weight": 60.0,
    "glucometer": 6.0
}
session = requests.session()
response = session.post('http://127.0.0.1:8000/device/add/', data=mea_data)
print('Create New Measurement for Patient for Patient ' + str(patient_id) + ': ')
print (response.url)
print (response.status_code)
print (response.headers)
print (response.text)