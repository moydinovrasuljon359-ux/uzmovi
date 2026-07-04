from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def navigation(request):
    return render(request, 'navigation.html')

def footer(request):
    return render(request, 'footer.html')

def index(request):
    return render(request,"index.html")

def category(request, category_name):
    return render(request, 'category.html')

def serial(request):
    return render(request,"serial.html")
def kinoyangilik(request):
    return render(request,"kinoyangilik.html")
def primyera(request):
    return render(request,"primyera.html")

def film(request):
    return render(request,"film.html")
def sms(request):
    return render(request,"sms.html")

def qoida(request):
    return render(request,"qoida.html")

def royhat(request):
    return render(request,"royhat.html")