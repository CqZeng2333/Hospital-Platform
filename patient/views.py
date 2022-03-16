from rest_framework import generics
from rest_framework.response import Response
from . import models
from . import serializers

# Create your views here.
class PatientList(generics.ListAPIView):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer

class PatientDetail(generics.RetrieveAPIView):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer