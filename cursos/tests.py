from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Curso, Modulo, Aula, Inscricao


class ControleAcessoAprendizagemTests(TestCase):

    def setUp(self):

        User = get_user_model()

        # Cria o primeiro usuário
        self.usuario = User.objects.create_user(
            username='aluno1',
            password='senha123'
        )

        # Cria o segundo usuário
        self.outro_usuario = User.objects.create_user(
            username='aluno2',
            password='senha123'
        )

        # Cria um curso publicado
        self.curso = Curso.objects.create(
            titulo='Curso de Python',
            descricao='Curso para aprender Python.',
            publicado=True
        )

        # Cria um módulo
        self.modulo = Modulo.objects.create(
            curso=self.curso,
            titulo='Introdução ao Python',
            descricao='Primeiro módulo do curso.',
            ordem=1
        )

        # Cria uma aula
        self.aula = Aula.objects.create(
            modulo=self.modulo,
            titulo='Primeira aula',
            conteudo='Conteúdo reservado da aula.',
            ordem=1
        )

        # Inscreve somente o primeiro usuário
        Inscricao.objects.create(
            usuario=self.usuario,
            curso=self.curso
        )

    def test_usuario_inscrito_acessa_area_aprendizagem(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'area_aprendizagem',
                kwargs={'curso_id': self.curso.id}
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Introdução ao Python')

    def test_usuario_nao_autenticado_nao_acessa_area(self):

        response = self.client.get(
            reverse(
                'area_aprendizagem',
                kwargs={'curso_id': self.curso.id}
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertIn('/accounts/login/', response.url)

    def test_usuario_nao_inscrito_nao_acessa_area(self):

        self.client.force_login(self.outro_usuario)

        response = self.client.get(
            reverse(
                'area_aprendizagem',
                kwargs={'curso_id': self.curso.id}
            ),
            follow=True
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Você precisa estar inscrito neste curso'
        )

    def test_usuario_inscrito_acessa_aula(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': self.aula.id}
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Conteúdo reservado da aula.'
        )

    def test_usuario_nao_autenticado_nao_acessa_aula(self):

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': self.aula.id}
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertIn('/accounts/login/', response.url)

    def test_usuario_nao_inscrito_nao_acessa_aula(self):

        self.client.force_login(self.outro_usuario)

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': self.aula.id}
            ),
            follow=True
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Você precisa estar inscrito neste curso'
        )

        self.assertNotContains(
            response,
            'Conteúdo reservado da aula.'
        )