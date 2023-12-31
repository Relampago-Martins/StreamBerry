from django.db.models import Sum, Count
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from streamberry.models import Filme, Streaming
from streamberry.serializers import FilmeSerializer, StreamingSerializer
from streamberry.filters import FilmeFilter


# Paginação para a API
class CustomPagination(PageNumberPagination):
    """
        Paginação customizada para a API
    """
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 250

# Views de acesso a API
class FilmeViewSet(viewsets.ModelViewSet):
    """
        CRUD para filmes
    """
    #pylint: disable=no-member
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    pagination_class = CustomPagination
    filterset_class = FilmeFilter

    @action(detail=False, methods=['get'])
    def nota_genero_ano(self, request):
        """
            Retorna a média de nota dos filmes por ano e genero
        """
        #pylint: disable=no-member
        filmes = Filme.objects.values('ano', 'genero').annotate(
            media_nota=Sum('avaliacoes__nota') / Count('avaliacoes__nota'))
        return Response(filmes)


class StreamingViewSet(viewsets.ModelViewSet):
    """
        CRUD para streamings
    """
    #pylint: disable=no-member
    queryset = Streaming.objects.all()
    serializer_class = StreamingSerializer
