from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def clinica(request):
    return render(request, 'clinica.html')

def pericia(request):
    return render(request, 'pericia.html')

def cursos(request):
    return render(request, 'cursos.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')
