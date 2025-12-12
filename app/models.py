from django.db import models

class Coche(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="coches/")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    # Datos opcionales si querés agregar más adelante:
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    año = models.IntegerField(blank=True, null=True)
    kilometros = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo
