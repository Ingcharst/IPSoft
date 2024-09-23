
from django.urls import path
from admision.views import ingreso_paciente

urlpatterns = [
    path('', ingreso_paciente, name='ingreso'),
]
