from django.shortcuts import render, HttpResponse

# Create your views here.
def home(requets):
    return HttpResponse('inicio')

def about(requets):
    return HttpResponse('About')

def services(requets):
    return HttpResponse('Services')

def store(requets):
    return HttpResponse('Store')

def contact(requets):
    return HttpResponse('Contactsto')

def blog(requets):
    return HttpResponse('blog')

def sample(requets):
    return HttpResponse('Pagina de prueba')