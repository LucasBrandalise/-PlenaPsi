from django.contrib import admin
from django.urls import path
from projeto import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.index, name='index'),
]
