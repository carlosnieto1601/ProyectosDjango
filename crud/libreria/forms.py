
from pprint import pformat
from django import forms
from .models import Estudiantes, Profesor,Asignaturas

class Estudiantesfrom(forms.ModelForm):
    class Meta:
        model= Estudiantes
        fields='__all__'

class Profesorfrom(forms.ModelForm):
    class Meta:
        model= Profesor
        fields='__all__'


class Asignaturasfrom(forms.ModelForm):
    class Meta:
        model= Asignaturas
        fields='__all__'