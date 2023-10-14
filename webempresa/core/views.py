from django.shortcuts import render, HttpResponse

# Create your views here.
def home(requets):
    return render(requets,'core/home.html')

def about(requets):
    return render(requets,'core/about.html')

def services(requets):
    return render(requets,'core/services.html')

def store(requets):
    return render(requets,'core/store.html')

def contact(requets):
    return render(requets,'core/contact.html')

def blog(requets):
    return render(requets,'core/blog.html')

def sample(requets):
    return render(requets,'core/sample.html')