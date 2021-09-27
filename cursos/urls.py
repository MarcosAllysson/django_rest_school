from django.urls import path
from cursos.views import home
from cursos.api.viewsets import (
    AvaliacaoAPIView,
    AvaliacoesAPIView,
    CursosAPIView,
    CursoAPIView,
    CursoViewSet,
    AvaliacaoViewSet,
)


# routers v2
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao')
]
