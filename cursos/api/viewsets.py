from rest_framework import mixins
from rest_framework import permissions

# VIEWSET, ROUTER
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response

from cursos.api.permissions import IsSuperUser
from cursos.api.serializers import CursoSerializer, AvaliacaoSerializer
from cursos.models import Curso, Avaliacao

"""
API V1
"""


class CursosAPIView(ListCreateAPIView):
    """
    Listagem e cria
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(RetrieveUpdateDestroyAPIView):
    """
    Pegar um só elemento, atualizar e ou deleta.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        """
        Listando todas as avaliações de um determinado curso
        """
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))

        return self.queryset.all()


class AvaliacaoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        """
        Trazendo todas as avaliações de um curso, filtrando pelo PK.
        """
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))

        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser, permissions.DjangoModelPermissions, )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # decoratador irá criar uma nova rota com o nome da função
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        """
        Retornando todas as avaliações do curso PK.
        .avaliacoes.all() -> related_name definido no models.py
        """

        # Paginação
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # curso = self.get_object()
        # serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer


class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

