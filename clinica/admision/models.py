from django.db import models

# Create your models here.

class Pacientes(models.Model):
    SEXO = [
        ('hombre', 'Masculino'),
        ('mujer', 'Femenino'),
        ('otro', 'Otro'),
        ('espera_triage', 'En Espera de Triage'),
    ]    
    documento = models.CharField(max_length=20, unique=True)    
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=20, choices=SEXO)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.nombre} ({self.documento})"



class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, related_name='historias_clinicas')
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    motivo_ingreso = models.TextField()
    diagnostico_inicial = models.CharField(max_length=255, blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    motivo_salida = models.CharField(max_length=255, blank=True, null=True)
    alta_medica = models.BooleanField(default=False)

    def __str__(self):
        return f"Historia de {self.paciente.nombre} ({self.fecha_ingreso.strftime('%Y-%m-%d %H:%M')})"





