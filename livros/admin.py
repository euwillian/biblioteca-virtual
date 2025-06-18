from django.contrib import admin
from .models import Livro
from emprestimos.models import Emprestimo
from django.contrib.auth import get_user_model

User = get_user_model()

"""
Django garante que está utilizando o modelo correto que foi configurado no settings.py

Explicao:

Ao registrar o model diretamente com from .models import User, você pode:
- Causar conflitos de importação entre apps
- Forçar o uso do modelo errado se houver ambiguidade
- Ter problemas ao usar bibliotecas que esperam o User correto

Como está utilizando AbstractUser, essa é a melhor forma
"""

admin.site.register(User)
admin.site.register(Livro)
admin.site.register(Emprestimo)
