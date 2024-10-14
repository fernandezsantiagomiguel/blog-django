from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    creado = models.DateTimeField("creado", auto_now_add=True)
    modificado = models.DateTimeField("modificado", auto_now=True)
    titulo = models.CharField(max_length=250)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="noticias")
    categorias = models.ManyToManyField(Categoria)
    visitas = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="not_megustas", blank=True
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False
    )

    def count_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo
 
    class Meta:
        permissions = [
            ('can_manage_noticias', 'can manage noticias'),
            ('can_manage_comentarios', 'Can manage comentarios'),
        ]