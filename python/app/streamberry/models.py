from django.db import models
from django.contrib.auth.models import User


#Modelos de dados
class Filme(models.Model):
    """
    Tabela de filmes
    """
    titulo = models.CharField(max_length=255, unique=True)
    mes = models.IntegerField(
        choices=[
            (1, "Janeiro"),
            (2, "Fevereiro"),
            (3, "Março"),
            (4, "Abril"),
            (5, "Maio"),
            (6, "Junho"),
            (7, "Julho"),
            (8, "Agosto"),
            (9, "Setembro"),
            (10, "Outubro"),
            (11, "Novembro"),
            (12, "Dezembro"),
        ]
    )
    ano = models.IntegerField()
    genero = models.CharField(max_length=255)
    streamings = models.ManyToManyField("Streaming", blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.titulo} ({self.ano})'

    def media_nota(self):
        """
        Calcula a média de nota do filme
        """
        #pylint: disable=no-member
        avaliacoes = self.avaliacoes.all()
        if avaliacoes:
            media = sum(a.nota for a in avaliacoes) / len(avaliacoes)
            return round(media, 2)
        return 0

    def count_streams(self):
        """
        Conta quantos streamings tem o filme
        """
        #pylint: disable=no-member
        return self.streamings.all().count()


class Avaliacao(models.Model):
    """
    Tabela de uma avaliação de um filme
    """
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name="avaliacoes")
    nota = models.FloatField( help_text="Nota de 0 a 5")
    comentario = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return f'{self.nota} - {self.comentario}'

class Streaming(models.Model):
    """
    Tabela para as plataformas de streamings de filmes
    """
    nome = models.CharField(max_length=255, unique=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.nome}'
