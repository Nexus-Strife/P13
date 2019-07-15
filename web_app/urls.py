from django.urls import path
from . import views

app_name = "web_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post_art, name='post'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
