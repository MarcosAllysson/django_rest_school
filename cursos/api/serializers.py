from rest_framework import serializers
from cursos.models import Curso, Avaliacao
from django.db.models import Avg


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        # não vai ser apresentado quando alguém visualizar. Questão de segurança, não é exibido.
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao

        # campos que serão mostrados
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

    # validando nota: (validate_NOME-DO-CAMPO)
    def validate_avaliacao(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5.')


class CursoSerializer(serializers.ModelSerializer):
    # Mostrar todas as avaliações de um curso na listagem (nested relationship)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related field
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Calculando média, cujo valor é gerado por uma função.
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    # Função para cálculo da média: PADRÃO - get_<NOME DO ATRIBUTO>
    def get_media_avaliacoes(self, obj):
        # avaliacoes, definido no related_name no models.py
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0

        return round(media * 2) / 2
