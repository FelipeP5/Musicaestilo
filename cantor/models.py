from django.db import models

class Cantor(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome
