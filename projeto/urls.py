from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clinicas/', views.clinica, name='clinica'),
    path('pericia/', views.pericia, name='pericia'),
    path('cursos/', views.cursos, name='cursos'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),

]