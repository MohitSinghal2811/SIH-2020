from django.urls import path
from . import views


urlpatterns = [
    path('', views.save_to_database, name = 'save_to_database'),
]