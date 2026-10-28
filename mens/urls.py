from django.urls import path
from . import views

urlpatterns = [
    path('',views.mens),
    path('footwears/',views.footwears),
    path('shoes/',views.shoes),
]