from django.db import models


class Pokemon(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.URLField()

    def __str__(self):
        return self.nome
