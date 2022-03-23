# Hospital-Platform

## Summary
* Platform to monitor patients at home or in the hospitals.

## Branching Strategy
* Add to main branch when function of module is well tested
* Ongoing function should be seen at dev branch
* Main: User module, Patient module, Device module
* Dev: Chat module

## Requirement
* Python 3.6, 3.7, 3.8
* Django 2.1
* djangorestframework 3.11.2
* SQLite3 3.7.17
* DeepSpeech 0.9.3

## Module
### [User](./user)
* Rest API of user module. 
* Sample usage in [user/example.py](./user/example.py).

|Method|Function|URL|Return Code|
|:-|:-|:-|:-|
|GET|Get all user(s)|/user/|200 OK|
|GET|Get a specific user|/user/{user_id}/|200 OK<br>404 Not Found|

### [Patient](./patient)
* Rest API of patient module. 
* Sample usage in [patient/example.py](./patient/example.py).

|Method|Function|URL|Return Code|
|:-|:-|:-|:-|
|GET|Get all patient(s)|/patient/|200 OK|
|GET|Get a specific patient|/patient/{patient_id}/|200 OK<br>404 Not found|

### [Device](./device)
* Rest API of device module.
* Sample usage in [device/example.py](./device/example.py).

|Method|Function|URL|Return Code|
|:-|:-|:-|:-|
|GET|Get measurement(s) for a patient|/device/patient-id/{patient_id}/|200 OK<br>400 No patient<br>404 No measurement for the patient|
|POST|Create new measurement for a patient|/device/measurement/add/|201 OK<br>400 No patient|

### [Chat](./chat)
* Rest API of chat module.
* Sample usage in [chat/example.py](./chat/example.py).

|Method|Function|URL|Return Code|
|:-|:-|:-|:-|
|GET|Get chat(s) from a user|/chat/from/{user_id}/|200 OK<br>400 No user<br>404 No chat for the user|
|GET|Get chat(s) to a user|/chat/to/{user_id}/|200 OK<br>400 No user<br>404 No chat for the user|
|POST|Create new chat for a user|/chat/add/|201 OK<br>400 No user|

### Speech-to-Text
* Sub-function to translate WAV-speech to text under Chat module.
* Prerequisite: download [DeepSpeech Model](https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm) and put it in [chat/model](./chat/model/) directory.
* Sample usage in [chat/example.py](./chat/example.py).

|Method|Function|URL|Return Code|
|:-|:-|:-|:-|
|POST|Translate WAV file(s) to text|/chat/audio-to-text/|200 OK<br>400 WAV file(s) restricted|