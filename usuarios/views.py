from django.shortcuts import render
from usuarios.models import Usuario

def usuario(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
    
    
    #return render(request, 'usuario.html', contexto)