# Hospital-Platform
## Branching Strategy
* Add to main branch when function of module is well tested
* Ongoing function should be seen at branches

## Requirement
* Python 3.6+
* Django
* djangorestframework

## Model
### [Device](./device)
* Local version API of device module. 

### [Patient](./patient)
* Local version API of patient module. 

### [Device API](./device_api)
* Rest API of device module.
* Include functions of creating new measurement records, and searching specific patients' measurement records.
* Sample usage in [example.py](./device_api/example.py). 