from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    numero=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    
    def __str__(self):
        fila="nombre: " + self.nombre +" - " + "apellido:"+ "-"+self.apellido
        return fila