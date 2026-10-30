from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.views.decorators.http import require_POST
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import CadastroForm


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

    next_url = (
        request.POST.get('next')
        or request.GET.get('next')
    )

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        form.error_messages['invalid_login'] = (
            'Usuário ou senha inválidos.'
        )

        form.error_messages['inactive'] = (
            'Esta conta está desativada.'
        )

        if form.is_valid():

            login(
                request,
                form.get_user()
            )

            messages.success(
                request,
                'Login realizado com sucesso!'
            )

            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure()
            ):

                return redirect(next_url)

            return redirect('accounts_home')

    else:

        form = AuthenticationForm(request)

        form.error_messages['invalid_login'] = (
            'Usuário ou senha inválidos.'
        )

        form.error_messages['inactive'] = (
            'Esta conta está desativada.'
        )

    return render(
        request,
        'accounts/login.html',
        {
            'form': form,
            'next': next_url
        }
    )


@login_required
@require_POST
def logout_usuario(request):

    logout(request)

    messages.success(
        request,
        'Você saiu da sua conta com sucesso.'
    )

    return redirect('accounts_home')