# HUDSON_HORNET/views.py
from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'HUDSON_HORNET/car_list.html', {'cars': cars})
