from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='accounts_home'
    ),

    path(
        'cadastro/',
        views.cadastro,
        name='cadastro'
    ),

    path(
        'login/',
        views.login_usuario,
        name='login'
    ),

    path(
        'logout/',
        views.logout_usuario,
        name='logout'
    ),

    path(
        'administracao/',
        views.painel_admin,
        name='painel_admin'
    ),

    path(
        'administracao/usuarios/',
        views.gerenciar_usuarios,
        name='gerenciar_usuarios'
    ),

    path(
        'administracao/usuarios/<int:usuario_id>/editar/',
        views.editar_usuario,
        name='editar_usuario'
    ),

]