from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, CommentsForm, SomeForm, TitleForm, PreviewForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as log
from django.contrib.auth import logout as out
from .models import Arts, Comments, Favs
from datetime import date
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    # List every articles on the website

    lst_art = Arts.objects.raw("SELECT waa.id, txt, title, preview, auth_user.username FROM web_app_arts waa "
                               "LEFT JOIN auth_user on waa.user_id = auth_user.id")

    paginator = Paginator(lst_art, 5)  # Show 5 articles per page

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'web_app/index.html', {'articles': articles})


def contact(request):
    return render(request, "web_app/contact.html")


def about(request):
    return render(request, "web_app/about.html")


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


@login_required(login_url='../login/')
def write_art(request):
    if request.method == 'POST':
        txt = SomeForm(request.POST)
        title = TitleForm(request.POST)
        preview = PreviewForm(request.POST)
        print(txt)
        print(title)
        print(preview)
        if txt.is_valid and title.is_valid and preview.is_valid:
            titl = title.cleaned_data['title']
            text = txt.cleaned_data['foo']
            prev = preview.cleaned_data['preview']
            current_user = request.user
            today = date.today()
            saveArt = Arts(txt=text, title=titl, user_id=current_user.id, date=today, preview=prev)
            saveArt.save()
            return redirect('../', locals())
        else:
            form = SomeForm()
            formTitle = TitleForm()
            formprev = PreviewForm()

    else:
        curr_user = request.user
        staff = curr_user.is_staff

        # Check if the user asking for the page is member of the staff. If not the user is redirected on the index
        if staff == True:
            form = SomeForm()
            formTitle = TitleForm()
            formprev = PreviewForm()
            return render(request, "web_app/write_art.html", locals())

        else:
            return redirect('../', locals())


def view_art(request, article):

    formCom = CommentsForm()
    reading_art = Arts.objects.filter(title__iexact=article).first()

    # Get the name of the user who posted the comment
    usr = Arts.objects.raw("SELECT au.id, username FROM auth_user au "
                           "LEFT JOIN web_app_arts ON au.id = web_app_arts.user_id WHERE web_app_arts.title = %s", (article, ))[0]

    # List every comments attached to the current article
    lst_comm = Comments.objects.raw("SELECT wac.id, comments, auth_user.username FROM web_app_comments wac "
                                    "LEFT JOIN web_app_arts p ON p.id = wac.art_id "
                                    "INNER JOIN auth_user on wac.user_id = auth_user.id WHERE wac.art_id = %s", (reading_art.id, ))
    return render(request, "web_app/post.html", locals())


def add_comm(request, article):
    if request.method == 'POST':
        form_com = CommentsForm(request.POST)
        if form_com.is_valid():
            current_user = request.user
            comment = form_com.cleaned_data['bodytxt']
            # Get the article's id
            art_id = Arts.objects.raw("SELECT id FROM web_app_arts WHERE title = %s", (article, ))[0]
            com = Comments(comments=comment, user_id=current_user.id, art_id=art_id.id)
            com.save()
            return redirect('../../view_art/' + article + '/')
        else:
            form_com = CommentsForm()
    else:
        pass


def add_fav(request):
    current_user = request.user
    id = request.GET.get('value')
    fav = Favs(art_id=id, user_id=current_user.id)
    fav.save()
    data = {'respond': id}
    return JsonResponse(data)


def profil(request):
    current_user = request.user

    # List every article faved by the user
    lst_fav = Favs.objects.raw("SELECT web_app_favs.id, art_id, web_app_favs.user_id,"
                               " web_app_arts.title, web_app_arts.txt FROM web_app_favs "
                               "LEFT JOIN web_app_arts ON art_id = web_app_arts.id WHERE web_app_favs.user_id = %s", (current_user.id, ))

    paginator = Paginator(lst_fav, 10)

    page = request.GET.get('page')
    favs = paginator.get_page(page)
    return render(request, 'web_app/profil.html', {'favs': favs})


def del_fav(request):
    id = request.GET.get('value')
    Favs.objects.filter(id=id).delete()
    data = {'respond': id}
    return JsonResponse(data)


def trigger_error(request):
    div_by_zero = 1 / 0

