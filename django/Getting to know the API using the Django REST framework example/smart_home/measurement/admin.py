from django.contrib import admin
from .models import Measurement, Sensor

@admin.register(Sensor)
class AdminSensor(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Measurement)
class AdminMeasurement(admin.ModelAdmin):
    list_display = ['id', 'sensor_id', 'temperature', 'date', 'photo']
