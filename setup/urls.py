from django.contrib import admin
from django.urls import path
from projeto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index.html', views.index, name='index'),
    path('clinica/', views.clinica, name='clinica'),
    path('pericia/', views.pericia, name='pericia'),
    path('cursos/', views.cursos, name='cursos'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]
