from django.shortcuts import render
from .models import Curso


def home(request):
    return render(request, 'cursos/home.html')


def catalogo(request):
    cursos = Curso.objects.filter(publicado=True)

    return render(request, 'cursos/catalogo.html', {'cursos': cursos})

def detalhes(request, curso_id):
    curso = Curso.objects.get(id=curso_id, publicado=True)

    return render(request, 'cursos/detalhes.html', {'curso': curso})