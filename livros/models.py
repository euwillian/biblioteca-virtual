from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.PositiveIntegerField() # Só aceitará números positivos
    categoria = models.CharField(max_length=30)
    
    # Por padrão do django, não preciso informar null=False ou blank=False
    
    def __str__(self):
        return f"{self.titulo} ({self.ano})"
