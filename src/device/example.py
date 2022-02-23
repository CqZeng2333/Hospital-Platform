import measurement as mea

if __name__ == '__main__':
    code = mea.insert_measurement_data(163949385, {
        'temperature': 36.8,
        'systolic blood pressure': 100,
        'diastolic blood pressure': 75,
        'pulse': 80,
        'oximeter': 96,
        'weight': 60,
        'glucometer': 6
    })
    print('Return code:' + str(code))