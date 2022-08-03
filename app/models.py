from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.URLField()

    def __str__(self):
        return self.nome