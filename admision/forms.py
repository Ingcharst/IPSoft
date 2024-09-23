
# ipsoftapp/forms.py

from django import forms
from .models import Pacientes

class PacienteForm(forms.ModelForm):
    motivo_ingreso = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), help_text="Indica el motivo del ingreso")

    class Meta:
        model = Pacientes
        fields = ['nombre', 'documento', 'fecha_nacimiento', 'sexo', 'direccion', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

