from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accounts_home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]