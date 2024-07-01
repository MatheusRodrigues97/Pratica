from django.shortcuts import render
from usuarios.froms import LoginForms, CadastroForms

def login(resquest):
    form = LoginForms()

    return render(resquest, 'usuarios/login.html',{'form': form})

def cadastro(request):
    form = CadastroForms()

    return render (request, 'usuarios/cadastro.html', {'form': form})

