from django.db import models
from django.core import validators

# Create your models here.
 
class Proyecto(models.Model):
    nombre = models.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(20)],max_length=20)
    apellido = models.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(20)],max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

