from django.shortcuts import render
from .models import Livro

def livro(request):
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        ano = request.POST.get("ano")
        categoria = request.POST.get("categoria")
        
        novo_livro = Livro(titulo=titulo, autor=autor, ano=ano, categoria=categoria)
        novo_livro.save()
    
    return render(request, 'novo_livro.html')