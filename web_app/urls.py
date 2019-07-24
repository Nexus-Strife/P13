from django.urls import path
from . import views

app_name = "web_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post_art, name='post'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('log_art_post/', views.login_art_post, name='art_logging'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('write/', views.write_art, name='write'),
    path('logout/', views.logout, name='logout'),

]
