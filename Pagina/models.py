from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts/')
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# Create your models here.
