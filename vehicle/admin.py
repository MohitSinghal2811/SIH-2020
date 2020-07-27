from django.contrib import admin
from .models import CarRTO, CarSurveillance, Camera

class CarRTOAdmin(admin.ModelAdmin):
    readonly_fields = ["DateRegistered", ]

class CarSurveillanceAdmin(admin.ModelAdmin):
    readonly_fields = ["FirstSeen", "LastSeen"]

admin.site.register(CarSurveillance, CarSurveillanceAdmin)
admin.site.register(CarRTO, CarRTOAdmin)
admin.site.register(Camera)