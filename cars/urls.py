from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
    path('brands/', views.brand_list, name='brand_list'),
]
