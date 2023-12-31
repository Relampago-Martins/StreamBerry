from django_filters import rest_framework as filters
from streamberry.models import Filme, Avaliacao

class FilmeFilter(filters.FilterSet):
    """
        Filtro para o model de filmes
        ref: https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html
    """
    class Meta:
        model = Filme
        fields = ['buscar', 'avaliacoes']

    buscar = filters.CharFilter(method='search_filter', field_name='buscar', label='Buscar')
    avaliacoes = filters.ModelChoiceFilter(
        queryset=Avaliacao.objects.distinct(),
        field_name='avaliacoes', label='Avaliações')

    def search_filter(self, queryset, _, value):
        """
            Busca multicampos: por título, ano e gênero
        """
        return queryset.filter(
            titulo__icontains=value, ano__icontains=value, genero__icontains=value)
