from django.shortcuts import render

def login(request):
    context = {}
    return render(request, 'myapp/login.html', context )
def navbar(request):
    context = {}
    return render(request, 'myapp/navbar.html' )
def home(request):
    context = {}
    return render(request, 'myapp/home.html' )
def profile(request):
    context = {}
    return render(request, 'myapp/profile.html')
