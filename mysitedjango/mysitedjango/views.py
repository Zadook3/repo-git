from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registration/registro.html')
