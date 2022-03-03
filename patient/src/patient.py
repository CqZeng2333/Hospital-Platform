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
        patient_ids = []
        with open('patient/data/patient_id.csv', 'r', encoding='utf8') as f:
            lines = f.readlines()[1:]
            for line in lines:
                patient_ids.append(int(line))
        if patient_id in patient_ids:
            return 200
        else:
            return 404
    else:
        return 400