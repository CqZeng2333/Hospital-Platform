import sys
import os
sys.path.append(os.getcwd() + '\src')
from patient.patient import is_valid_patient_id

def get_measurements_data_by_patient_id(patient_id):
    pass

def get_measurement_data_by_measurement_id(patient_id):
    pass

'''
Interface for devices to ingest data into the system

Parameters:
patient_id: the id of patient to find
mea_data: a dictionary in format of data_field.sample_data.measurement

Return:
200: Sucessful operation
400: Invalid ID supplied
404: Patient not found
405: Invalid data format
'''
def insert_measurement_data(patient_id, mea_data):
    if type(patient_id) == int and type(mea_data) == dict:
        is_valid = is_valid_patient_id(patient_id)
        if is_valid != 200:
            return is_valid # 404
        '''insert into database'''
        pass
        return 200
    elif type(patient_id) != int:
        return 400
    else:
        return 405

class Measurement(object):
    def _init_(self, data):
        self.patient_id = data['patient_id']
        self.measurement = data['measurement']