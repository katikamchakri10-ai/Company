from django.urls import path
from . import views

urlpatterns = [
    path('',views.electronics),
    path('laptop/',views.laptop),
    path('tv/',views.tv),
    path('fridge/',views.fridge),
    path('ac/',views.ac)
]