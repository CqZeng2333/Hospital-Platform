from django.db import models

class Measurement(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    temperature = models.FloatField(null=True, blank=True)
    systolic_blood_pressure = models.FloatField(null=True, blank=True)
    diastolic_blood_pressure = models.FloatField(null=True, blank=True)
    pulse = models.FloatField(null=True, blank=True)
    oximeter = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    glucometer = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.patient_id) + ' ' + str(self.updated_at)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)