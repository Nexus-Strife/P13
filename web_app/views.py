from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "web_app/index.html")


def post_art(request):
    return render(request, "web_app/post.html")


def contact(request):
    return render(request, "web_app/contact.html")


def about(request):
    return render(request, "web_app/about.html")