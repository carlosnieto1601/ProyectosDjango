from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,verbose_name='Nombre')
    apellido=models.CharField(max_length=100,verbose_name='Apellido')
    numero=models.CharField(max_length=100,verbose_name='Numero')
    correo=models.CharField(max_length=100,verbose_name='Correo')
    
    def __str__(self):
        fila="nombre: " + self.nombre +" - " + "apellido:"+ "-"+self.apellido
        return fila

class clases(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    estudiante=models.CharField(max_length=100)
    asignatura=models.CharField(max_length=100)
   