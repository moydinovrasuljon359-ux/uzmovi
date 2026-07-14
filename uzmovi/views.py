from django.shortcuts import get_object_or_404, render
from .models import *
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


def videoichi(request):
    return render(request, "videoichi.html")
def splash(request):
    return render(request,"splash.html")

def index(request):
    bannerlar = Banner.objects.all()
    return render(request, "index.html", {
        "bannerlar": bannerlar,
    })
from django.shortcuts import render
from .models import Kino

def index(request):
    kinolar = Kino.objects.select_related(
        "janr",
        "davlat",
        "yil"
    ).all()

    return render(request, "videoichi.html", {
        "kinolar": kinolar
    })