#models.py
from django.db import models

class Laboratorio(models.Model):
    clave_id = models.IntegerField(default=0) 
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)  # Nuevo campo
    pais = models.CharField(max_length=255)    # Nuevo campo

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=255)  # Nuevo campo

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)
