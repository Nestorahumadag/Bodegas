from django.db import models
from django.contrib.auth.models import User

class TipoBodega(models.Model):

    tipo = models.CharField(max_length=100)
    metros_cuadrados = models.PositiveIntegerField()
    preparada_quimicos = models.BooleanField(default=False)
    preparada_organico = models.BooleanField(default=False)
    hermetica = models.BooleanField(default=False)
    precio_mensual = models.PositiveIntegerField()
    
    

    def __str__(self):
        return f"{self.tipo} - {self.precio_mensual} CLP"

class Bodega(models.Model):
    codigo_unico = models.CharField(max_length=100, unique=True)
    tipo = models.ForeignKey(TipoBodega, on_delete=models.CASCADE)
    descripcion = models.TextField(default='Sin descripción')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Bodega {self.codigo_unico} ({self.tipo})"

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='noticias/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Like(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, related_name='likes', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'noticia')

    def __str__(self):
        return f"{self.usuario.username} le dio like a {self.noticia.titulo}"
