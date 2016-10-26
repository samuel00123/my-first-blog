from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre      = models.CharField(max_length=200)
    apellidos   = models.CharField(max_length=200)
    status      = models.BooleanField(default=True)

    def __str__(self):
        nombreCompleto= "%s %s"%(self.nombre,self.apellidos)
        return nombreCompleto


class Producto(models.Model):
    nombre      = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=200)
    status      = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
