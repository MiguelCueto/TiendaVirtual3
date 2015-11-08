from django.db import models

# Create your models here.
class Proveedor(models.Model):
	nombre=models.CharField(max_length=50)
	direccion=models.CharField(max_length=50)
	telefono=models.IntegerField()
	nombre_articulo=models.CharField(max_length=50)
	precio=models.FloatField()

class Articulo(models.Model):
	TIPO_CHOICES=(
	('N','Nuevo'),
	('U','Usado'),
	)
	nombre=models.CharField(max_length=50)
	fecha=models.DateField()
	precio=models.FloatField()
	tipo=models.CharField(max_length=1, choices=TIPO_CHOICES)
	