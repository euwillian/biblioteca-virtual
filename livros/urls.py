from django.urls import path
from livros.views import livro

urlpatterns = [
    path('novo_livro/', livro, name='novo_livro'),
]