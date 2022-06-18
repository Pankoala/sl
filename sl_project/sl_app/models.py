from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    """ Define la tabla Perfil """
    nombreCliente = models.CharField(max_length=20, default="Nombre de Cliente")
    fechaNacimiento = models.DateField(null=True, blank=True)
    GENERO = [
        ("H", "Hombre"),
        ("M", "Mujer"),
        ("O", "Otro"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)
    TIPO = [
        ("PF", "Persona Física"),
        ("PM", "Persona Moral"),
    ]
    tipo = models.CharField(max_length=45, choices=TIPO, null=True, blank=True)

    def __str__(self):
        return self.nombreCliente


class Tarjeta(models.Model):
    """Define la tabla de Tarjeta"""
    nombreTarjeta = models.CharField(max_length=145)
    descripcion = models.CharField(max_length=256)
    interes = models.FloatField(default=0.0)

    def __str__(self):
        return self.nombreTarjeta


class ClienteTarjeta(models.Model):
    """ Define tabla conjunta de Cliente y Tarjeta"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    numeroTarjeta = models.IntegerField()
    creditoMax = models.FloatField(null = True, blank = True)

    def __str__(self):
        return str(self.numeroTarjeta)


