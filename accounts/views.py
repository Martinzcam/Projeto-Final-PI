from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from cursos.models import Curso, Modulo, Aula

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import CadastroForm, UsuarioForm
from .decorators import admin_required

def home(request):

    return render(
        request,
        'accounts/home.html'
    )


def cadastro(request):

    if request.user.is_authenticated:
        return redirect('accounts_home')

    if request.method == 'POST':

        form = CadastroForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Cadastro realizado com sucesso! Agora você pode fazer login.'
            )

            return redirect('login')

    else:

        form = CadastroForm()

    return render(
        request,
        'accounts/cadastro.html',
        {'form': form}
    )


def login_usuario(request):

    if request.user.is_authenticated:
        return redirect('accounts_home')

    next_url = request.POST.get('next') or request.GET.get('next')

    form = AuthenticationForm(
        request,
        data=request.POST if request.method == 'POST' else None
    )

    form.error_messages['invalid_login'] = 'Usuário ou senha inválidos.'
    form.error_messages['inactive'] = 'Esta conta está desativada.'

    if request.method == 'POST' and form.is_valid():

        login(request, form.get_user())

        messages.success(request, 'Login realizado com sucesso!')

        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()
        ):
            return redirect(next_url)

        return redirect('accounts_home')

    return render(request, 'accounts/login.html', {
        'form': form,
        'next': next_url
    })


@login_required
@require_POST
def logout_usuario(request):

    logout(request)

    messages.success(
        request,
        'Você saiu da sua conta com sucesso.'
    )

    return redirect('accounts_home')

@admin_required
def painel_admin(request):

    contexto = {
        'total_usuarios': get_user_model().objects.count(),
        'total_cursos': Curso.objects.count(),
        'total_modulos': Modulo.objects.count(),
        'total_aulas': Aula.objects.count(),
    }

    return render(
        request,
        'accounts/painel_admin.html',
        contexto
    )

@admin_required
def gerenciar_usuarios(request):

    usuarios = get_user_model().objects.all()

    return render(
        request,
        'accounts/gerenciar_usuarios.html',
        {'usuarios': usuarios}
    )

@admin_required
def editar_usuario(request, usuario_id):

    usuario = get_object_or_404(
        get_user_model(),
        id=usuario_id
    )

    if usuario.is_staff or usuario.is_superuser:
        raise PermissionDenied

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            return redirect('gerenciar_usuarios')

    else:
        form = UsuarioForm(instance=usuario)

    return render(
        request,
        'accounts/form_usuario.html',
        {'form': form}
    )