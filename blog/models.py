from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
# Objeto
class Post(models.Model):
    # Link para outro modelo
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Texto com número limitado de caracteres.
    title = models.CharField(max_length=200)
    # Campo para texto sem limite fixo.
    text = models.TextField()
    # Date e hora.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Método
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title