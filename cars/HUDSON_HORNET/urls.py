# HUDSON_HORNET/urls.py
from django.urls import path
from .views import car_list

urlpatterns = [
    path('calculator/', car_list, name='car_list'),
]
