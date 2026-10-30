from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Curso, Inscricao


def home(request):
    return render(request, 'cursos/home.html')


def catalogo(request):
    cursos = Curso.objects.filter(publicado=True)

    return render(request, 'cursos/catalogo.html', {'cursos': cursos})


def detalhes(request, curso_id):
    curso = get_object_or_404(
        Curso,
        id=curso_id,
        publicado=True
    )

    return render(request, 'cursos/detalhes.html', {'curso': curso})


@login_required
@require_POST
def inscrever(request, curso_id):

    curso = get_object_or_404(
        Curso,
        id=curso_id,
        publicado=True
    )

    inscricao, criada = Inscricao.objects.get_or_create(
        usuario=request.user,
        curso=curso
    )

    if criada:
        messages.success(
            request,
            'Inscrição realizada com sucesso!'
        )
    else:
        messages.error(
            request,
            'Você já está inscrito neste curso.'
        )

    return redirect('detalhes', curso_id=curso.id)


@login_required
def meus_cursos(request):

    inscricoes = Inscricao.objects.filter(
        usuario=request.user
    ).select_related('curso').order_by('-data_inscricao')

    return render(
        request,
        'cursos/meus_cursos.html',
        {'inscricoes': inscricoes}
    )