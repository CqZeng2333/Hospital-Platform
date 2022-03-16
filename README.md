# Hospital-Platform

## Branching Strategy
* Add to main branch when function of module is well tested
* Ongoing function should be seen at dev branch
* Main: User module, Patient module, Device module
* Dev: Chat module

## Requirement
* Python 3.6+
* Django 2.2.5
* djangorestframework 3.13.1

## Model
### [User](./user)
* Rest API of user module. 
* Sample usage in [example.py](./user/example.py).

|Method|Function|URL|
|:-|:-|:-|
|GET|Get all user(s)|/user/|
|GET|Get a specific user|/user/{user_id}/|

### [Patient](./patient)
* Rest API of patient module. 
* Sample usage in [example.py](./patient/example.py).

|Method|Function|URL|
|:-|:-|:-|
|GET|Get all patient(s)|/patient/|
|GET|Get a specific patient|/patient/{patient_id}/|

### [Device](./device)
* Rest API of device module.
* Sample usage in [example.py](./device/example.py).

|Method|Function|URL|
|:-|:-|:-|
|GET|Get measurement(s) for a specific patient|/device/patient-id/{patient_id}/|
|POST|Create new measurement for a specific patient|/device/measurement/add/|