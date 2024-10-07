from django.db import models
from estilo.models import Estilo
from cantor.models import Cantor

class Musica(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE, default='funk')
    cantor = models.ForeignKey(Cantor, on_delete=models.SET_DEFAULT, default='Fernando&César')

    def __str__(self):
        return self.nome
