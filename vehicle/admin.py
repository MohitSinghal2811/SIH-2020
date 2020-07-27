from django.contrib import admin
from .models import CarRTO, CarSurveillance, Camera


admin.site.register(CarSurveillance)
admin.site.register(CarRTO)
admin.site.register(Camera)