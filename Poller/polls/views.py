from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import *
# Create your views here.

def home_page(request):
    return render(request, "home_page.html")

def available_polls_page(request):
    queryset= Question.objects.all()
    # print (queryset)

    return render(request, "available_polls_page.html", {'questions': queryset})

def voting_page(request, id):
    question = get_object_or_404(Question, pk=id)
    if request.method=="POST":

        selected_choice = question.choices_set.get(pk=request.POST['voted_choice'])
        # print(selected_choice)
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('post_vote_page', args=(question.id,)))




    # queryset=Choices.objects.all()
    # queryset= Question.objects.get(pk=id)
    # print(queryset)
    return render(request, "voting_page.html", {'questions': question})


def post_vote_page(request, id):
    queryset= Question.objects.get(pk=id)
    return render(request, "post_vote_page.html", {'questions': queryset})

def result_page(request, id):
    queryset=Question.objects.get(pk=id)
    return render(request, "result_page.html", {'questions': queryset})

def resultsData(request, id):
    votedata = []

    question = Question.objects.get(id=id)
    votes = question.choices_set.all()

    for i in votes:
        votedata.append({i.choice_text:i.votes})

    print(votedata)
    return JsonResponse(votedata, safe=False)