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
        'aula/<int:aula_id>/',
        views.detalhe_aula,
        name='detalhe_aula'
    ),

]