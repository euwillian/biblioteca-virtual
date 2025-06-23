from django.urls import path
from livros.views import livro, editar_livro, excluir_livro

urlpatterns = [
    path('novo_livro/', livro, name='novo_livro'),
    path('editar_livro/<int:id>', editar_livro, name='editar_livro'),
    path('excluir_livro/<int:id>', excluir_livro, name='excluir_livro'),
]

"""

Quando você define <int:alguma_coisa> na URL, o Django passa isso como argumento nomeado para a sua função.

Se estiver <int:livro_id>, o Django faz:

editar_livro(request, livro_id=123)
Então sua função precisa aceitar exatamente esse nome (livro_id), ou dará erro.


"""