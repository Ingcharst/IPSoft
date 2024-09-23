from django.shortcuts import render, redirect
from .models import Pacientes, HistoriaClinica
from .forms import PacienteForm
from django.contrib import messages

# Create your views here.

def ingreso_paciente(request):
    if request.method == 'POST':
        formulario = PacienteForm(request.POST)
        if formulario.is_valid():
            paciente = formulario.save()
            
            # Crear automáticamente la Historia Clínica
            HistoriaClinica.objects.create(
                paciente=paciente,
                motivo_ingreso=formulario.cleaned_data.get('motivo_ingreso', '')
            )
            messages.success(request, 'Paciente registrado exitosamente y historia clínica creada.')
            return redirect('dashboard')  # Redirigir a la vista que prefieras después de registrar
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        formulario = PacienteForm()
    
    return render(request, 'admision/ingreso_paciente.html', {'formulario': formulario})
