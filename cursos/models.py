from django.db import models
from django.conf import settings


class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Modulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.IntegerField()

    def __str__(self):
        return self.titulo


class Aula(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    ordem = models.IntegerField()
    video_url = models.URLField(blank=True)

    def __str__(self):
        return self.titulo


class Inscricao(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE
    )

    data_inscricao = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'curso'],
                name='inscricao_unica_por_usuario_curso'
            )
        ]

    def __str__(self):
        return f'{self.usuario.username} - {self.curso.titulo}'