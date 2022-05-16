
from ast import Delete
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Estudiantes, Profesor, Asignaturas
from .forms import Asignaturasfrom, Estudiantesfrom, Profesorfrom
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def inicio(request):
  return render(request,'paginas/inicio.html')

def registrar(request):
    if request.method== 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            messages.success(request, f'usuario {username} creado')
    else:
        form = UserCreationForm()
    
    context = {'form':form}
    return render(request,'registro/index.html',context)

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def estudiantes(request):
    estudiantes=Estudiantes.objects.all()
    #print(estudiantes)
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
    #clases=clases.objects.all()
    return render(request, 'clases/index.html')

def profesor(request):
    profesor=Profesor.objects.all()
    return render(request, 'profesor/index.html', {'profesor':profesor})

def crear_profesor(request):
    formulario1= Profesorfrom(request.POST or None)
    if formulario1.is_valid():
        formulario1.save()
        return redirect('profesor')
    return render(request,'profesor/crear.html', {'formulario1':formulario1})

def eliminarp(request, id):
    profesor=Profesor.objects.get(id=id)
    profesor.delete()
    return redirect('profesor')

def editarp(request,id):
    profesor= Profesor.objects.get(id=id)
    formulario1= Profesorfrom(request.POST or None, request.FILES or None, instance=profesor)
    print(formulario1.is_valid())
    if formulario1.is_valid() and request.POST:
        formulario1.save()
        return redirect('profesor')
    else:
        print('no es valido')
    return render(request,'profesor/editar.html',{'formulario1':formulario1})



def asignaturas(request):
    asignaturas=Asignaturas.objects.all()
    #print(estudiantes)
    return render(request, 'asignaturas/index.html', {'asignaturas': asignaturas})

def crear_asignatura(request):
    formulario2= Asignaturasfrom(request.POST or None)
    if formulario2.is_valid():
        formulario2.save()
        return redirect('asignaturas')
    return render(request,'asignaturas/crear.html', {'formulario2':formulario2})


def eliminara(request, id):
    asignaturas=Asignaturas.objects.get(id=id)
    asignaturas.delete()
    return redirect('asignaturas')

def editara(request,id):
    asignaturas= Asignaturas.objects.get(id=id)
    formulario2= Asignaturasfrom(request.POST or None, request.FILES or None, instance=asignaturas)
    print(formulario2.is_valid())
    if formulario2.is_valid() and request.POST:
        formulario2.save()
        return redirect('asignaturas')
    else:
        print('no es valido')
    return render(request,'asignaturas/editar.html',{'formulario2':formulario2})