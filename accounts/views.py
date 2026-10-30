from django.shortcuts import render

def home(request):
    return render(request, 'accounts/home.html')

def cadastro(request):
    return render(request, 'accounts/cadastro.html')


def login_usuario(request):
    return render(request, 'accounts/login.html')


def logout_usuario(request):
    return render(request, 'accounts/home.html')