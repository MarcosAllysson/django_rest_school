from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cursos.models import Curso, Avaliacao
from cursos.api.serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de cursos.
    """

    # Método HTTP GET
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)  # passando todos os cursos (many)

        return Response(serializer.data)

    def post(self, request):
        # pegando dados da request e serializando
        serializer = CursoSerializer(data=request.data)

        # verificando se é válido. Se não for, levanta exceção
        serializer.is_valid(raise_exception=True)

        # sendo válido, salve-os
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de avaliação
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
