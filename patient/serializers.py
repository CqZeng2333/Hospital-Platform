from rest_framework import serializers
from . import models

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user_id')
        model = models.Patient