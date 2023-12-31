from django.urls import include, path
from rest_framework import routers
from streamberry import views

router = routers.DefaultRouter()
router.register(r'filmes', views.FilmeViewSet, basename='filmes')
router.register(r'streamings', views.StreamingViewSet, basename='streamings')

urlpatterns = [
    path('', include(router.urls)),
]
