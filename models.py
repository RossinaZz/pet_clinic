from django.db import models

class Pets(models.Model):
    raza=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    consulta=models.CharField(max_length=200)

class Veterinary(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    matricula=models.IntegerField()

class Client(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email= models.EmailField()
    numerocliente=models.IntegerField()
