import datetime 
from django.shortcuts import render
from django.http import HttpResponse
import random
from ynav.models import Question

def questions(request):
  q = Question(question_text="Do you love Django", pub_date=datetime.datetime.now())
  q.save()
  q.choice_set.create(choice_text="yes", votes=10)
  q.choice_set.create(choice_text="no", votes=1)
  q.save()
  context = {"q": Question.objects.all() }
  return render(request, "questions.html", context)

def create_question_form(request):
  render(request, "create_question_form.html")

def about(request):
  return render(request, "about.html")

def dynamic(request):
  context = {"i" : random.randint(1, 10) , "t": "hello"}
  return render(request, "dynamic.html", context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
  return HttpResponse("<h1>Hello, world.</h1>")

def user_profile(request):
  return HttpResponse("""
  <head>
      <title>Profile</title>
  </head>
  <body>
      <h1 style="color:red">Profile</h1>
      <p>First Name: John</p>
      <p>Last Name: Doe</p>
  </body>
  </html>
  """)

