from django.contrib.auth.models import AbstractUser

"""
Essa classe está herdando da AbstractUser para criar um novo usuário
Com todas permissoes, validacoes, campos etc.
"""
class Usuario(AbstractUser):
    def __str__(self):
        return self.username