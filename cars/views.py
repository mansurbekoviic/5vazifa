from django.shortcuts import render
from .models import Car, Brand

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'cars/brand_list.html', {'brands': brands})
