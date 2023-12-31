from rest_framework import serializers
from streamberry.models import Filme, Streaming, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    """
        Serializer para o model de avaliações
    """
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']

    nota = serializers.FloatField(min_value=0, max_value=5)


class StreamingSerializer(serializers.ModelSerializer):
    """
        Serializer para o model de streamings
    """
    class Meta:
        model = Streaming
        fields = ['nome']


class FilmeSerializer(serializers.ModelSerializer):
    """
        Serializer para o model de filmes
    """
    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'mes', 'ano', 'genero', 'avaliacoes', 'streamings',
                  'media_nota', 'count_streams']

    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    streamings = StreamingSerializer(many=True, read_only=True)
