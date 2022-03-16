# Hospital-Platform
## Branching Strategy
* Add to main branch when function of module is well tested
* Ongoing function should be seen at dev branch
* Main: User module, Patient module, Device module
* Dev: Chat module

## Requirement
* Python 3.6+
* Django
* djangorestframework

## Model
### [User](./user)
* Rest API of user module. 

### [Patient](./patient)
* Rest API of patient module. 

### [Device](./device)
* Rest API of device module.
* Include functions of creating new measurement records, and searching specific patients' measurement records.
* Sample usage in [example.py](./device/example.py). 