from django.urls import  path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('registrar', views.registrar, name='registrar'),
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('estudiantes/crear', views.crear_estudiante, name='crear_estudiante'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('estudiantes/editar/<int:id>', views.editar, name='editar'),
    path('clases', views.clases, name='clases'),
    path('profesor', views.profesor, name='profesor'),
    path('profesor/crear', views.crear_profesor, name='crear_profesor'),
    path('eliminarp/<int:id>', views.eliminarp, name='eliminarp'),
    path('editarp/editar/<int:id>', views.editarp, name='editarp'),
    path('asignaturas', views.asignaturas, name='asignaturas'),
    path('asignaturas/crear', views.crear_asignatura, name='crear_asignatura'),
    path('elimara/<int:id>', views.eliminara, name='eliminara'),
    path('editara/editar/<int:id>', views.editara, name='editara'),
]