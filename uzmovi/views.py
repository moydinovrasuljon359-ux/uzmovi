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