
from django.contrib import admin
from django.urls import path
from the_weather import views
urlpatterns = [
    path('', views.weather, name='weather'),
]
