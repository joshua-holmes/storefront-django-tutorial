from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question

# Create your views here.
def say_hello(request):
  print("HERE", request)
  x = 1
  y = 2
  return render(request, 'hello.html')

def index(request):
  question_list = Question.objects.order_by('-pub_date')[:5]
  context = {
    'question_list': question_list
  }
  return render(request, 'playground/index.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'playground/detail.html', {'question': question})

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)