from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='cursos_home'
    ),

    path(
        'catalogo/',
        views.catalogo,
        name='catalogo'
    ),

    path(
        'detalhes/<int:curso_id>/',
        views.detalhes,
        name='detalhes'
    ),

    path(
        'inscrever/<int:curso_id>/',
        views.inscrever,
        name='inscrever'
    ),

    path(
        'meus-cursos/',
        views.meus_cursos,
        name='meus_cursos'
    ),

    path(
        'aprender/<int:curso_id>/',
        views.area_aprendizagem,
        name='area_aprendizagem'
    ),

    path(
        'modulo/<int:modulo_id>/',
        views.detalhe_modulo,
        name='detalhe_modulo'
    ),

    path(
        'aula/<int:aula_id>/',
        views.detalhe_aula,
        name='detalhe_aula'
    ),

    path(
        'gerenciar/',
        views.gerenciar_cursos,
        name='gerenciar_cursos'
    ),

    path(
        'gerenciar/criar/',
        views.criar_curso,
        name='criar_curso'
    ),

    path(
        'gerenciar/<int:curso_id>/editar/',
        views.editar_curso,
        name='editar_curso'
    ),

    path(
        'gerenciar/<int:curso_id>/excluir/',
        views.excluir_curso,
        name='excluir_curso'
    ),

    # Gerenciamento de módulos

    path(
        'gerenciar/modulos/',
        views.gerenciar_modulos,
        name='gerenciar_modulos'
    ),

    path(
        'gerenciar/modulos/criar/',
        views.criar_modulo,
        name='criar_modulo'
    ),

    path(
        'gerenciar/modulos/<int:modulo_id>/editar/',
        views.editar_modulo,
        name='editar_modulo'
    ),

    path(
        'gerenciar/modulos/<int:modulo_id>/excluir/',
        views.excluir_modulo,
        name='excluir_modulo'
    ),

    # Gerenciamento de aulas

    path(
        'gerenciar/aulas/',
        views.gerenciar_aulas,
        name='gerenciar_aulas'
    ),

    path(
        'gerenciar/aulas/criar/',
        views.criar_aula,
        name='criar_aula'
    ),

    path(
        'gerenciar/aulas/<int:aula_id>/editar/',
        views.editar_aula,
        name='editar_aula'
    ),

    path(
        'gerenciar/aulas/<int:aula_id>/excluir/',
        views.excluir_aula,
        name='excluir_aula'
    ),
]