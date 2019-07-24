from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, CommentsForm, SomeForm, TitleForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as log
from django.contrib.auth import logout as out
from .models import Arts
from datetime import date


# Create your views here.


def index(request):
    return render(request, "web_app/index.html", locals())


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

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['nickname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                            last_name=last_name)
            return redirect('../login/')
        else:
            pass
    else:
        form = RegisterForm()

    return render(request, "web_app/register.html", locals())


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['nickname']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                log(request, user)
                return redirect('../')
            else:
                pass
        else:
            pass
    else:
        form = LoginForm()

    return render(request, "web_app/login.html", locals())


def logout(request):
    out(request)
    return redirect("../")


def write_art(request):
    if request.method == 'POST':
        txt = SomeForm(request.POST)
        title = TitleForm(request.POST)
        print(txt)
        print(title)
        if txt.is_valid and title.is_valid:
            titl = title.cleaned_data['title']
            text = txt.cleaned_data['foo']
            current_user = request.user
            today = date.today()
            saveArt = Arts(txt=text, title=titl, user_id=current_user.id, date=today)
            saveArt.save()
            return render(request, 'web_app/index.html', locals())
        else:
            form = SomeForm()
            formTitle = TitleForm()

    else:
        form = SomeForm()
        formTitle = TitleForm()
    return render(request, "web_app/write_art.html", locals())

