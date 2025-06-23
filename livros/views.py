from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro

def livro(request):
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        ano = request.POST.get("ano")
        categoria = request.POST.get("categoria")
        
        novo_livro = Livro(titulo=titulo, autor=autor, ano=ano, categoria=categoria)
        novo_livro.save()
        
    listar_livros = Livro.objects.all()
    # Busca todos livros
        
    contexto = {
        'livros': listar_livros,
        }
        
    return render(request, 'novo_livro.html', contexto)


def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    
    if request.method == 'POST':
        # pegar tudo que o usuário esta enviado no POST via GET
        livro.titulo = request.POST.get("titulo")
        livro.autor = request.POST.get("autor")
        livro.ano = request.POST.get("ano")
        livro.categoria = request.POST.get("categoria")
        livro.save()
        
        return redirect('novo_livro') # volta para a página principal
    
    contexto = {'livro': livro,}
    
    return render(request, 'editar_livro.html', contexto)


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    
    if request.method == 'POST':
        # pegar tudo que o usuário esta enviado no POST via GETlivro.titulo = request.POST.get("titulo")
        livro.autor = request.POST.get("autor")
        livro.ano = request.POST.get("ano")
        livro.categoria = request.POST.get("categoria")
        livro.delete()
        
        return redirect('novo_livro') # volta para a página principal
    

    contexto = {'livro': livro,}
    return render(request, 'excluir_livro.html', contexto)