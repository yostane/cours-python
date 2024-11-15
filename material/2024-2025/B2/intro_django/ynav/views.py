import datetime 
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random
from ynav.froms import QuestionForm
from ynav.models import Question

def questions(request):
  context = {"q": Question.objects.all() }
  return render(request, "questions.html", context)

def submit_question(request):
  if request.method == "POST":
    form = QuestionForm(request.POST)
    if form.is_valid():
      q = Question(question_text=form.cleaned_data["question"], pub_date=datetime.datetime.now())
      q.save()
      q.choice_set.create(choice_text=form.cleaned_data["choice1"], votes=form.cleaned_data["votes1"])
      q.choice_set.create(choice_text=form.cleaned_data["choice2"], votes=form.cleaned_data["votes2"])
      q.save()
  return questions(request)

def create_question_form(request):
  return render(request, "create_question_form.html")

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
  <html>
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

def show_time(request: HttpRequest) -> HttpResponse:
  return render(request, "time.html", {"time": datetime.datetime.now().strftime('%H:%M')})

def show_p_param(request: HttpRequest) -> HttpResponse:
  p_value = request.GET.get("p")
  return render(request, "showp.html", {"p": p_value})
