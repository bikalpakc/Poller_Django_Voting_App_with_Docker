from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def home_page(request):
    return render(request, "home_page.html")

def available_polls_page(request):
    queryset= Question.objects.all()
    # print (queryset)

    return render(request, "available_polls_page.html", {'questions': queryset})

def voting_page(request, id):
    if request.method=="POST":
        Question.objects.get(pk=id)
        voted_choice=request.POST.get('voted_choice')
        selected_choice_object=Choices.objects.get(choice_text=voted_choice)
        selected_choice_object.votes=int(selected_choice_object.votes) + 1
        selected_choice_object.save()
        Choices.save()

        return redirect("/voted/")




    # queryset=Choices.objects.all()
    queryset= Question.objects.get(pk=id)
    # print(queryset)
    return render(request, "voting_page.html", {'questions': queryset})


def post_vote_page(request, id):
    queryset= Question.objects.get(pk=id)
    return render(request, "post_vote_page.html", {'questions': queryset})

def result_page(request, id):
    queryset=Question.objects.get(pk=id)
    return render(request, "result_page.html", {'questions': queryset})