from django.db import models
from django.contrib.auth.models import User
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
	nombre=models.ManyToManyField(Proveedor)
	nombre=models.CharField(max_length=50)
	fecha=models.DateTimeField(auto_now=True)
	precio=models.FloatField()
	tipo=models.CharField(max_length=1, choices=TIPO_CHOICES)
	user=models.ForeignKey(User, default=1)
	
