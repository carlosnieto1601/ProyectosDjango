
from django import forms
from .models import Estudiantes

class Estudiantesfrom(forms.ModelForm):
    class Meta:
        model= Estudiantes
        fields='__all__'

