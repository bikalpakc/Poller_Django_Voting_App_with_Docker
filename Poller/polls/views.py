from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, "home_page.html")

def available_polls_page(request):
    return render(request, "available_polls_page.html")
