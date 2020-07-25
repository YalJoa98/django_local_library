from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=25)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='mariabonita')
    precio = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    fechaNacimiento = models.DateField()

