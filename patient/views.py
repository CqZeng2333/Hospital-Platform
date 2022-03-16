from rest_framework import generics
from . import models
from . import serializers
#from rest_framework.response import Response

# Create your views here.
class PatientList(generics.ListAPIView):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer

class PatientDetail(generics.RetrieveAPIView):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer