from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, CommentsForm

# Create your views here.


def index(request):
    return render(request, "web_app/index.html")


def post_art(request):
    return render(request, "web_app/post.html")


def contact(request):
    return render(request, "web_app/contact.html")


def about(request):
    return render(request, "web_app/about.html")


def login_art_post(request):
    form = LoginForm()
    return render(request, "web_app/log_art.html", locals())


def register(request):
    form = RegisterForm()
    return render(request, "web_app/register.html", locals())


def login(request):
    form = LoginForm()
    return render(request, "web_app/login.html", locals())
