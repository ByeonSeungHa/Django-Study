from django.urls import path
from . import views

urlpatterns = [
    path('Pig/', views.Pig),
    path('', views.landing),
]