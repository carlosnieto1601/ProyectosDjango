
from django.http import HttpResponse
from django.shortcuts import render
from .models import Estudiantes
# Create your views here.

def inicio(request):
  return render(request,'paginas/inicio.html')


def nosotros(request):
    return render(request,'paginas/nosotros.html')

def estudiantes(request):
    estudiantes=Estudiantes.objects.all()
    # print(estudiantes)
    return render(request, 'estudiantes/index.html', {'estudiantes': estudiantes})

def crear_estudiante(request):
    return render(request,'estudiantes/crear.html')

def editar(request):
    return render(request,'estudiantes/editar.html')