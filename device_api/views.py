# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from . import models
from . import serializers

class MeasureList(generics.ListAPIView):
    queryset = models.Measurement.objects.all()
    serializer_class = serializers.MeasurementSerializer

class MeasureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Measurement.objects.all()
    serializer_class = serializers.MeasurementSerializer

class MeasureForPatient(generics.ListAPIView):
    serializer_class = serializers.MeasurementSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        queryset = models.Measurement.objects.filter(patient_id=int(patient_id))
        return queryset

    def get(self, request, patient_id):
        # patient_id = self.kwargs['patient_id']
        if not patient_id:
            return Response(status=400, data='Incorrect patient ID. ')
        else:
            patient = models.Patient.objects.filter(id=int(patient_id))
            if not patient.exists():
                return Response(status=400, data='Patient does not exist. ')
        
        objects = self.get_queryset()
        if not objects.exists():
            return Response(status=404, data='No measurement for the patient. ')
        serializer = self.get_serializer(objects, many=True)
        return Response(data=serializer.data)

class AddMeasurementView(generics.CreateAPIView): 
    serializer_class = serializers.MeasurementSerializer

class PatientList(generics.ListAPIView):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer