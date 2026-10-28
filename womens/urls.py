from django.urls import path
from . import views

urlpatterns = [
    path('',views.womens),
    path('handbags/',views.handbags),
    path('cosmetics/',views.cosmetics),
]