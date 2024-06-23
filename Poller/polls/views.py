from django.shortcuts import render
from .models import *
# Create your views here.

def home_page(request):
    return render(request, "home_page.html")

def available_polls_page(request):
    queryset= Question.objects.all()
    # print (queryset)

    return render(request, "available_polls_page.html", {'questions': queryset})

def voting_page(request):
    return render(request, "voting_page.html")
