from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Curso, Modulo, Aula, Inscricao


class InterfaceAprendizagemTests(TestCase):

    def setUp(self):

        User = get_user_model()

        # Cria o aluno inscrito.
        self.usuario = User.objects.create_user(
            username='aluno1',
            password='senha123'
        )

        # Cria um segundo aluno sem inscrição.
        self.outro_usuario = User.objects.create_user(
            username='aluno2',
            password='senha123'
        )

        # Cria o curso publicado.
        self.curso = Curso.objects.create(
            titulo='Curso de Python',
            descricao='Aprenda Python.',
            publicado=True
        )

        # Cria os módulos.
        self.modulo1 = Modulo.objects.create(
            curso=self.curso,
            titulo='Introdução ao Python',
            descricao='Primeiros passos com Python.',
            ordem=1
        )

        self.modulo2 = Modulo.objects.create(
            curso=self.curso,
            titulo='Fundamentos de Python',
            descricao='Conceitos fundamentais.',
            ordem=2
        )

        # Cria um módulo sem aulas.
        self.modulo_vazio = Modulo.objects.create(
            curso=self.curso,
            titulo='Módulo extra',
            descricao='Módulo ainda sem conteúdo.',
            ordem=3
        )

        # Cria as aulas.
        self.aula1 = Aula.objects.create(
            modulo=self.modulo1,
            titulo='O que é Python?',
            conteudo='Conteúdo da primeira aula.',
            ordem=1,
            video_url='https://example.com/video-python'
        )

        self.aula2 = Aula.objects.create(
            modulo=self.modulo1,
            titulo='Instalação do Python',
            conteudo='Conteúdo da segunda aula.',
            ordem=2,
            video_url=''
        )

        self.aula3 = Aula.objects.create(
            modulo=self.modulo2,
            titulo='Variáveis',
            conteudo='Conteúdo sobre variáveis.',
            ordem=1,
            video_url=''
        )

        # Inscreve somente o primeiro usuário.
        Inscricao.objects.create(
            usuario=self.usuario,
            curso=self.curso
        )

    def test_aluno_inscrito_acessa_area_aprendizagem(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'area_aprendizagem',
                kwargs={'curso_id': self.curso.id}
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'cursos/area_aprendizagem.html'
        )

    def test_modulos_aparecem_em_ordem(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'area_aprendizagem',
                kwargs={'curso_id': self.curso.id}
            )
        )

        modulos = list(response.context['modulos'])

        self.assertEqual(
            [modulo.titulo for modulo in modulos],
            [
                'Introdução ao Python',
                'Fundamentos de Python',
                'Módulo extra'
            ]
        )

    def test_usuario_deslogado_nao_acessa_area(self):

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

        self.assertContains(
            response,
            'Você precisa estar inscrito neste curso'
        )

    def test_aluno_inscrito_acessa_modulo(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_modulo',
                kwargs={'modulo_id': self.modulo1.id}
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'cursos/modulo.html'
        )

    def test_aulas_aparecem_em_ordem(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_modulo',
                kwargs={'modulo_id': self.modulo1.id}
            )
        )

        aulas = list(response.context['aulas'])

        self.assertEqual(
            [aula.titulo for aula in aulas],
            [
                'O que é Python?',
                'Instalação do Python'
            ]
        )

    def test_usuario_nao_inscrito_nao_acessa_modulo(self):

        self.client.force_login(self.outro_usuario)

        response = self.client.get(
            reverse(
                'detalhe_modulo',
                kwargs={'modulo_id': self.modulo1.id}
            ),
            follow=True
        )

        self.assertContains(
            response,
            'Você precisa estar inscrito neste curso'
        )

    def test_modulo_inexistente_retorna_404(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_modulo',
                kwargs={'modulo_id': 99999}
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_modulo_sem_aulas_exibe_mensagem(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_modulo',
                kwargs={'modulo_id': self.modulo_vazio.id}
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Este módulo ainda não possui aulas cadastradas.'
        )

    def test_navegacao_entre_modulos(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_modulo',
                kwargs={'modulo_id': self.modulo1.id}
            )
        )

        self.assertIsNone(
            response.context['modulo_anterior']
        )

        self.assertEqual(
            response.context['proximo_modulo'],
            self.modulo2
        )

    def test_aluno_inscrito_acessa_aula(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': self.aula1.id}
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'cursos/aula.html'
        )

        self.assertContains(
            response,
            'Conteúdo da primeira aula.'
        )

    def test_video_aparece_quando_existe_url(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': self.aula1.id}
            )
        )

        self.assertContains(
            response,
            'https://example.com/video-python'
        )

        self.assertContains(
            response,
            'Assistir vídeo da aula'
        )

    def test_video_nao_aparece_sem_url(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': self.aula2.id}
            )
        )

        self.assertNotContains(
            response,
            'Assistir vídeo da aula'
        )

    def test_navegacao_entre_aulas(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': self.aula2.id}
            )
        )

        self.assertEqual(
            response.context['aula_anterior'],
            self.aula1
        )

        # A próxima aula pertence ao módulo seguinte.
        self.assertEqual(
            response.context['proxima_aula'],
            self.aula3
        )

    def test_usuario_nao_inscrito_nao_acessa_aula(self):

        self.client.force_login(self.outro_usuario)

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': self.aula1.id}
            ),
            follow=True
        )

        self.assertContains(
            response,
            'Você precisa estar inscrito neste curso'
        )

        self.assertNotContains(
            response,
            'Conteúdo da primeira aula.'
        )

    def test_usuario_deslogado_nao_acessa_aula(self):

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': self.aula1.id}
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertIn('/accounts/login/', response.url)

    def test_aula_inexistente_retorna_404(self):

        self.client.force_login(self.usuario)

        response = self.client.get(
            reverse(
                'detalhe_aula',
                kwargs={'aula_id': 99999}
            )
        )

        self.assertEqual(response.status_code, 404)