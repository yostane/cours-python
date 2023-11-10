from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("prompt-input", views.showQueryForm, name="prompt-input"),
    path("run-query", views.processQueryForm, name="run-query"),
    path("ai-chat", views.showChatView, name="ai-chat"),
]
