from django.contrib import admin
from .models import Curso, Modulo, Aula, Inscricao


admin.site.register(Curso)
admin.site.register(Modulo)
admin.site.register(Aula)
admin.site.register(Inscricao)