from django.db import models

# Create your models here.

class Paciente(models.Model):
    ESTADO = [
        ('atencion', 'En Atención'),
        ('observacion', 'En Observación'),
        ('espera_atencion', 'En Espera de Atención'),
        ('espera_triage', 'En Espera de Triage'),
        ('hospitalizado', 'Hospitalizados'),
        ('cirugia', 'En Cirugía'),
        ('uci', 'En UCI'),
        #('alta', 'En Espera de Triage'),
    ]
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO)

    def __str__(self):
        return self.nombre
