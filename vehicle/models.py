from django.db import models
from django.urls import reverse


class CarRTO(models.Model):

    # Fields
    Brand = models.CharField(max_length=20, null = False, blank = False)
    Owner = models.CharField(max_length=30, null = False, blank = False)
    DateRegistered = models.DateTimeField(auto_now_add=True)
    CarModel = models.CharField(max_length=20, null = False, blank = False)
    PlateNumber = models.CharField(max_length=10, unique = True, primary_key = True,  null = False, blank  = False)
    Color = models.CharField(max_length=10, null = False, blank = False)

    def __str__(self):
        return str(self.pk)


class CarSurveillance(models.Model):

    # Fields
    LastSeen = models.DateTimeField(auto_now=True, editable=False)
    Color = models.CharField(max_length=10)
    CarModel = models.CharField(max_length=20)
    FirstSeen = models.DateTimeField(auto_now_add=True, editable=False)
    PlateNumber = models.CharField(max_length=10, null = False, blank = False, primary_key = True, unique = True)
    Brand = models.CharField(max_length=20)
    CameraID = models.CharField(max_length = 10, null=False, blank=False)

    def __str__(self):
        return str(self.pk)

class Camera(models.Model):

    # Fields
    Location = models.TextField(max_length=100)
    CameraID = models.CharField(max_length = 10, primary_key=True)

    def __str__(self):
        return str(self.pk)
