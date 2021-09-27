from django.contrib import admin
from cursos.models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')
