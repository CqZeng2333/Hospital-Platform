from rest_framework import serializers
from . import models

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'patient_id',
        "temperature","systolic_blood_pressure","diastolic_blood_pressure","pulse","oximeter","weight","glucometer",
        'created_at', 'updated_at',)
        model = models.Measurement