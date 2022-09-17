from django.shortcuts import render

def index(request):
    return render (request,'index.html')

def sucodelaranja(request):
    return render (request, 'sucodelaranja.html')

def sucodelimao(request):
    return render(request, 'sucodelimao.html')

def sucodeabacaxi(request):
    return render (request, 'sucodeabacaxi.html')

def sucodemorango(request):
    return render(request, 'sucodemorango.html')

def contato(request):
    return render(request, 'contato.html')