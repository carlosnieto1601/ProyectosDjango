
from ast import Delete
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Estudiantes, clases
from .forms import Estudiantesfrom

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
    formulario= Estudiantesfrom(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('estudiantes')
    return render(request,'estudiantes/crear.html', {'formulario':formulario})

def eliminar(request, id):
    estudiante=Estudiantes.objects.get(id=id)
    estudiante.delete()
    return redirect('estudiantes')


def editar(request,id):
    estudiante= Estudiantes.objects.get(id=id)
    formulario= Estudiantesfrom(request.POST or None, request.FILES or None, instance=estudiante)
    print(formulario.is_valid())
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('estudiantes')
    else:
        print('no es valido')
    return render(request,'estudiantes/editar.html',{'formulario':formulario})

def clases(request):
    # clases=clases.objects.all()
    return render(request, 'clases/index.html')

def profesor(request):
    return render(request, 'profesor/index.html')

def asignaturas(request):
    return render (request, 'asignaturas/index.html')

