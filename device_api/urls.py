from django.urls import path
from . import views

urlpatterns = [
    path('', views.MeasureList.as_view()),
    path('patient-id/<int:patient_id>/', views.MeasureForPatient.as_view()),
    path('patient/', views.PatientList.as_view()),
    path('add/', views.AddMeasurementView.as_view()),
]