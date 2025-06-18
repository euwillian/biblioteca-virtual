from django.db import models
from django.conf import settings
from livros.models import Livro 

class Emprestimo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # no db vai como usuario_id
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos') # livro_id
    data_emprestimo = models.DateTimeField(auto_now_add=True) 
    data_devolucao = models.DateTimeField()

    def __str__(self):
        return f"{self.usuario} - {self.livro} - ({self.data_devolucao.date()})"
     # o .date() é para converter somente para pegar a data
