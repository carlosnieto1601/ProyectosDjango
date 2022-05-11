from django.urls import  path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('estudiantes/crear', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar', views.editar, name='editar'),

]