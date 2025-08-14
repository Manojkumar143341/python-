from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('navbar/', views.navbar, name='navbar'),
     path('home/', views.home, name='home'),
     path('profile/', views.profile, name='profile'),

]