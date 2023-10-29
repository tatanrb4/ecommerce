from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=75, blank=False, null=False)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=75, blank=False, null=False)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    urlImagen = models.URLField(null=False, blank=False)
    promocion = models.BooleanField(blank=False, null=False, default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.nombre
