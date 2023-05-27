from django.db import models
import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    descripcion = RichTextUploadingField(null=True, blank=True)
    imagen_portada = models.ImageField(null=True, blank=True, default="default_image.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    #author = User.objects.create_user("Juan", "jnovelli@gmail.com", "contraseñajuan")

    def __str__(self) -> str:
        return self.titulo


