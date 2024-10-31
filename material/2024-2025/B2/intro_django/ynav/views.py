from django.shortcuts import render
from django.http import HttpResponse
import random

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

