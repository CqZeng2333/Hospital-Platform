from django.urls import path
from . import views

urlpatterns = [
    path('measurement/', views.MeasureList.as_view()),
    path('patient-id/<int:patient_id>/', views.MeasureForPatient.as_view()),
    path('measurement/add/', views.AddMeasurementView.as_view()),
]