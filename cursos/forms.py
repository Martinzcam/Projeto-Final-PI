from django import forms
from .models import Curso, Modulo, Aula


class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ['titulo', 'descricao', 'publicado']

class ModuloForm(forms.ModelForm):

    class Meta:
        model = Modulo
        fields = ['curso', 'titulo', 'descricao', 'ordem']


class AulaForm(forms.ModelForm):

    class Meta:
        model = Aula
        fields = [
            'modulo',
            'titulo',
            'conteudo',
            'ordem',
            'video_url'
        ]