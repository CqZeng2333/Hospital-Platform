'''
Interface to validate if the patient_id is valid

Parameters:
patient_id: the id of patient to find

Return:
200: valid patient id
400: Invalid ID supplied
404: Patient not found
'''
def is_valid_patient_id(patient_id):
    if type(patient_id) == int:
        if patient_id == 163949385:
            return 200
        else:
            return 404
    else:
        return 400