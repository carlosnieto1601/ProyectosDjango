from django.urls import  path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('estudiantes/crear', views.crear_estudiante, name='crear_estudiante'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('estudiantes/editar/<int:id>', views.editar, name='editar'),
    path('clases', views.clases, name='clases'),
    path('profesor', views.profesor, name='profesor'),
    path('asignaturas', views.asignaturas, name='asignaturas'),

]