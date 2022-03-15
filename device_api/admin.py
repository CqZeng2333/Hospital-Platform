from django.contrib import admin

# Register your models here.
from . models import Measurement
admin.site.register(Measurement)

from . models import Patient
admin.site.register(Patient)