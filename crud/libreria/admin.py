from django.contrib import admin
from .models import Estudiantes, Asignaturas, Profesor
# Register your models here.

admin.site.register(Estudiantes)
admin.site.register(Asignaturas)
admin.site.register(Profesor)

