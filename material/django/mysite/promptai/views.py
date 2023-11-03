from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .forms import PromptForm
from .models import Prompt


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {"prompts": Prompt.objects.all()}
    return HttpResponse(template.render(context, request))


def showQueryForm(request):
    return render(request, "prompt-input.html")


def processQueryForm(request):
    form = PromptForm(request.POST)
    if not form.is_valid():
        return HttpResponse(f"<h1>Invalid</h1>")
    user = User.objects.all()[1]
    user.prompt_set.create(query=form.cleaned_data["query"], reply="réponse à la main")
    user.save()
    return HttpResponse(f"<h1>The query was: {form.cleaned_data['query']}</h1>")
