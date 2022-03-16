# from django.test import TestCase

# Create your tests here.
import pytest
import requests

def test_success_get_patient_measurement():
    patient_id = 1
    session = requests.session()
    response = session.get('http://127.0.0.1:8000/device/patient-id/' + str(patient_id))
    assert response.status_code == 200

def test_get_patient_not_exist_measurement():
    patient_id = 4
    session = requests.session()
    response = session.get('http://127.0.0.1:8000/device/patient-id/' + str(patient_id))
    assert response.status_code == 400

def test_get_patient_measurement_not_exist():
    patient_id = 3
    session = requests.session()
    response = session.get('http://127.0.0.1:8000/device/patient-id/' + str(patient_id))
    assert response.status_code == 404

# def test_create_patient_measurement_success():
#     mea_data = {
#         "patient_id": 1,
#         "temperature": 36.9,
#         "systolic_blood_pressure": 101.0,
#         "diastolic_blood_pressure": 78.0,
#         "pulse": 80.0,
#         "oximeter": 96.0,
#         "weight": 60.0,
#         "glucometer": 6.0
#     }
#     session = requests.session()
#     response = session.post('http://127.0.0.1:8000/device/add/', data=mea_data)
#     assert response.status_code == 201

def test_create_patient_not_exist_measurement():
    mea_data = {
        "patient_id": 4,
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
    assert response.status_code == 400

if __name__ == '__main__':
    pytest.main(['device_project/device_api/tests.py', '-s'])