from django.shortcuts import render
from personal.models import Empleado

# Create your views here.

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'personal/lista_empleados.html', {'empleados': empleados})

