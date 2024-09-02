from django.db import models

# Create your models here.

class Profesion(models.Model):
    codigo = models.CharField(max_length=20)
    nombre_profesion = models.CharField(max_length=50)
  
    def __str__(self):
        return self.nombre_profesion


class Especialidad(models.Model):
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    nombre_especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_especialidad


class Empleado(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    #fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"