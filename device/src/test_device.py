import pytest
import measurement as mea

def test_insert_data():
    code = mea.insert_measurement_data(163949385, {
        'temperature': 36.8,
        'systolic blood pressure': 100,
        'diastolic blood pressure': 75,
        'pulse': 80,
        'oximeter': 96,
        'weight': 60,
        'glucometer': 6
    })
    assert code == 200

def test_insert_data_patient_not_found():
    code = mea.insert_measurement_data(160000000, {
        'temperature': 36.8,
        'systolic blood pressure': 100,
        'diastolic blood pressure': 75,
        'pulse': 80,
        'oximeter': 96,
        'weight': 60,
        'glucometer': 6
    })
    assert code == 404

def test_insert_data_invalid_patient_Id():
    code = mea.insert_measurement_data(None, {
        'temperature': 36.8,
        'systolic blood pressure': 100,
        'diastolic blood pressure': 75,
        'pulse': 80,
        'oximeter': 96,
        'weight': 60,
        'glucometer': 6
    })
    assert code == 400

def test_insert_data_invalid_data_format():
    code = mea.insert_measurement_data(163949385, None)
    assert code == 405

if __name__ == '__main__':
    pytest.main(['device/src/test_device.py', '-s'])

