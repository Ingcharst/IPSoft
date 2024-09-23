from django.shortcuts import render
from ipsoftapp.models import Paciente
from django.db.models import Count
import json

# Create your views here.

def index(request):
    estados = Paciente.objects.values('estado').annotate(count=Count('id'))
    estadocounts = {estado['estado']: estado['count'] for estado in estados}
    
    estado_counts = json.dumps(estadocounts)

    return render(request, 'ipsoftapp/index.html', {
        'estado_counts': estado_counts
    })

"""
def pacientes(request):
    estados = Paciente.objects.values('estado').annotate(count=Count('id'))
    estado_counts = {estado['estado']: estado['count'] for estado in estados}

    return render(request, 'ipsoftapp/dashboard.html', {
        'estado_counts': estado_counts
    })
"""