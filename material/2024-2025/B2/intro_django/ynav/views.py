import datetime 
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random
from ynav.froms import QuestionForm, NameForm
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

def show_query_profile(request: HttpRequest) -> HttpResponse:
  context = { "fn": request.GET.get("first_name"), "ln": request.GET.get("last_name") }
  return render(request, "query_profile.html", context)

def show_range(request: HttpRequest) -> HttpResponse:
  start = int(request.GET.get("min"))
  end = int(request.GET.get("max"))
  context = { "r": range(start, end + 1) }
  return render(request, "range.html", context)


def name_form(request: HttpRequest) -> HttpResponse:
  if request.method == "POST":
    form = NameForm(request.POST)
    if form.is_valid():
      return render(request, "nameformresult.html", {"name": form.cleaned_data["name"]})
  return render(request, "nameform.html")