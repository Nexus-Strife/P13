from django.urls import path
from . import views

app_name = "web_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('log_art_post/', views.login_art_post, name='art_logging'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('write/', views.write_art, name='write'),
    path('logout/', views.logout, name='logout'),
    path('view_art/<article>/', views.view_art, name='view_art'),
    path('add_comm/<article>/', views.add_comm, name='add_comm'),
    path('add_fav/', views.add_fav, name='add_fav'),
    path('profil/', views.profil, name='profil'),
    path('del_fav/', views.del_fav, name='del_fav'),


]
