from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Prefetch

from .models import Curso, Modulo, Aula, Inscricao


def home(request):
    return render(request, 'cursos/home.html')


def catalogo(request):
    cursos = Curso.objects.filter(publicado=True)

    return render(
        request,
        'cursos/catalogo.html',
        {'cursos': cursos}
    )


def _usuario_inscrito_no_curso(usuario, curso):
    return Inscricao.objects.filter(
        usuario=usuario,
        curso=curso
    ).exists()


def detalhes(request, curso_id):
    curso = get_object_or_404(
        Curso,
        id=curso_id,
        publicado=True
    )

    inscrito = False

    if request.user.is_authenticated:
        inscrito = _usuario_inscrito_no_curso(
            request.user,
            curso
        )

    return render(
        request,
        'cursos/detalhes.html',
        {
            'curso': curso,
            'inscrito': inscrito
        }
    )


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


@login_required
def area_aprendizagem(request, curso_id):
    curso = get_object_or_404(
        Curso,
        id=curso_id,
        publicado=True
    )

    if not _usuario_inscrito_no_curso(request.user, curso):
        messages.error(
            request,
            'Você precisa estar inscrito neste curso para acessar a área de aprendizagem.'
        )

        return redirect('detalhes', curso_id=curso.id)

    modulos = Modulo.objects.filter(
        curso=curso
    ).order_by('ordem', 'id').prefetch_related(
        Prefetch(
            'aula_set',
            queryset=Aula.objects.order_by('ordem', 'id')
        )
    )

    return render(
        request,
        'cursos/area_aprendizagem.html',
        {
            'curso': curso,
            'modulos': modulos
        }
    )


@login_required
def detalhe_modulo(request, modulo_id):
    modulo = get_object_or_404(
        Modulo.objects.select_related('curso'),
        id=modulo_id,
        curso__publicado=True
    )

    curso = modulo.curso

    if not _usuario_inscrito_no_curso(request.user, curso):
        messages.error(
            request,
            'Você precisa estar inscrito neste curso para acessar este módulo.'
        )

        return redirect('detalhes', curso_id=curso.id)

    aulas = Aula.objects.filter(
        modulo=modulo
    ).order_by('ordem', 'id')

    modulos = list(
        Modulo.objects.filter(
            curso=curso
        ).order_by('ordem', 'id')
    )

    indice = next(
        i for i, item in enumerate(modulos)
        if item.id == modulo.id
    )

    modulo_anterior = (
        modulos[indice - 1] if indice > 0 else None
    )

    proximo_modulo = (
        modulos[indice + 1]
        if indice < len(modulos) - 1
        else None
    )

    return render(
        request,
        'cursos/modulo.html',
        {
            'curso': curso,
            'modulo': modulo,
            'aulas': aulas,
            'modulo_anterior': modulo_anterior,
            'proximo_modulo': proximo_modulo
        }
    )


@login_required
def detalhe_aula(request, aula_id):
    aula = get_object_or_404(
        Aula.objects.select_related('modulo__curso'),
        id=aula_id,
        modulo__curso__publicado=True
    )

    curso = aula.modulo.curso

    if not _usuario_inscrito_no_curso(request.user, curso):
        messages.error(
            request,
            'Você precisa estar inscrito neste curso para acessar esta aula.'
        )

        return redirect('detalhes', curso_id=curso.id)

    # Busca todas as aulas do curso na ordem dos módulos e das aulas.
    aulas_curso = list(
        Aula.objects.filter(
            modulo__curso=curso
        ).select_related(
            'modulo'
        ).order_by(
            'modulo__ordem',
            'modulo__id',
            'ordem',
            'id'
        )
    )

    # Descobre a posição da aula atual.
    indice = next(
        i for i, item in enumerate(aulas_curso)
        if item.id == aula.id
    )

    # Identifica a aula anterior e a próxima.
    aula_anterior = (
        aulas_curso[indice - 1] if indice > 0 else None
    )

    proxima_aula = (
        aulas_curso[indice + 1]
        if indice < len(aulas_curso) - 1
        else None
    )

    return render(
        request,
        'cursos/aula.html',
        {
            'aula': aula,
            'curso': curso,
            'modulo': aula.modulo,
            'aula_anterior': aula_anterior,
            'proxima_aula': proxima_aula
        }
    )