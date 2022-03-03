import sys
import os
sys.path.append(os.getcwd())
from patient.src.patient import is_valid_patient_id

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
        
        # insert into database
        insert_str = ""
        insert_str += str(get_max_measurement_id() + 1) + ','
        insert_str += str(patient_id) + ','

        keys = {"temperature","systolic blood pressure","diastolic blood pressure","pulse","oximeter","weight","glucometer"}
        for key in keys:
            if mea_data[key] == None:
                insert_str += ','
            else:
                insert_str += str(mea_data[key]) + ','
        insert_str = insert_str[:-1] + '\n'
        with open('device/data/measurement.csv', 'a', encoding='utf8') as f:
            f.write(insert_str)
        
        # Successfully insert
        return 200
    elif type(patient_id) != int:
        return 400
    else:
        return 405

def get_max_measurement_id():
    with open('device/data/measurement.csv', 'r', encoding='utf8') as f:
        lines = f.readlines()
    if len(lines) == 1:
        return 0
    else:
        line = lines[-1].split(',')
        return int(line[0])

class Measurement(object):
    def _init_(self, data):
        self.patient_id = data['patient_id']
        self.measurement = data['measurement']