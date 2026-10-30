from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class TestesAutenticacao(TestCase):

    def setUp(self):

        self.usuario = User.objects.create_user(
            username='aluno_teste',
            email='aluno@email.com',
            password='SenhaForte@2026'
        )

    def test_pagina_cadastro_abre(self):

        response = self.client.get(
            reverse('cadastro')
        )

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'accounts/cadastro.html'
        )

    def test_cadastro_com_dados_validos(self):

        dados = {
            'username': 'novo_aluno',
            'email': 'novo@email.com',
            'password1': 'Curso@2026Seguro',
            'password2': 'Curso@2026Seguro'
        }

        response = self.client.post(
            reverse('cadastro'),
            dados,
            follow=True
        )

        self.assertRedirects(
            response,
            reverse('login')
        )

        usuario_criado = User.objects.get(
            username='novo_aluno'
        )

        self.assertEqual(
            usuario_criado.email,
            'novo@email.com'
        )

        self.assertTrue(
            usuario_criado.check_password(
                'Curso@2026Seguro'
            )
        )

        self.assertContains(
            response,
            'Cadastro realizado com sucesso'
        )

    def test_cadastro_com_email_duplicado(self):

        dados = {
            'username': 'outro_aluno',
            'email': 'aluno@email.com',
            'password1': 'Curso@2026Seguro',
            'password2': 'Curso@2026Seguro'
        }

        response = self.client.post(
            reverse('cadastro'),
            dados
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Este e-mail já está cadastrado.'
        )

        self.assertFalse(
            User.objects.filter(
                username='outro_aluno'
            ).exists()
        )

    def test_cadastro_com_senhas_diferentes(self):

        dados = {
            'username': 'aluno_invalido',
            'email': 'invalido@email.com',
            'password1': 'Curso@2026Seguro',
            'password2': 'OutraSenha@2026'
        }

        response = self.client.post(
            reverse('cadastro'),
            dados
        )

        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            response.context['form'].errors
        )

        self.assertFalse(
            User.objects.filter(
                username='aluno_invalido'
            ).exists()
        )

    def test_login_pagina_abre(self):

        response = self.client.get(
            reverse('login')
        )

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'accounts/login.html'
        )

    def test_login_com_credenciais_corretas(self):

        dados = {
            'username': 'aluno_teste',
            'password': 'SenhaForte@2026'
        }

        response = self.client.post(
            reverse('login'),
            dados,
            follow=True
        )

        self.assertRedirects(
            response,
            reverse('accounts_home')
        )

        self.assertIn(
            '_auth_user_id',
            self.client.session
        )

        self.assertContains(
            response,
            'Login realizado com sucesso!'
        )

    def test_login_com_senha_incorreta(self):

        dados = {
            'username': 'aluno_teste',
            'password': 'SenhaErrada'
        }

        response = self.client.post(
            reverse('login'),
            dados
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Usuário ou senha inválidos.'
        )

        self.assertNotIn(
            '_auth_user_id',
            self.client.session
        )

    def test_logout_encaminha_para_pagina_inicial(self):

        self.client.force_login(self.usuario)

        response = self.client.post(
            reverse('logout'),
            follow=True
        )

        self.assertRedirects(
            response,
            reverse('accounts_home')
        )

        self.assertNotIn(
            '_auth_user_id',
            self.client.session
        )

        self.assertContains(
            response,
            'Você saiu da sua conta com sucesso.'
        )

    def test_logout_nao_aceita_get(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse('logout')
        )

        self.assertEqual(response.status_code, 405)

    def test_usuario_autenticado_nao_acessa_cadastro(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse('cadastro')
        )

        self.assertRedirects(
            response,
            reverse('accounts_home')
        )

    def test_usuario_autenticado_nao_acessa_login(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse('login')
        )

        self.assertRedirects(
            response,
            reverse('accounts_home')
        )