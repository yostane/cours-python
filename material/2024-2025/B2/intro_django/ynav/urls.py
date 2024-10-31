from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello", views.hello, name="hello"),
    path("user/profile", views.user_profile, name="user_profile"),
    path("about", views.about, name="about"),
    path("dynamic", views.dynamic, name="dynamic"),
    path("questions", views.questions, name="questions"),
]