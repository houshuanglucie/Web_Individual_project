from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


# connection view
def connection(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
        return render(request, 'taskmanager/projects.html', locals())
    return render(request, 'taskmanager/login.html', locals())


# disconnection view
def disconnection(request):
    logout(request)
    return render(request, 'taskmanager/login.html', locals())


# list of projects
def projects(request):
    pass
    return render(request, 'taskmanager/projects.html', locals())


# List of tasks in one project
def project(request):
    pass
    return render(request, 'taskmanager/project.html', locals())


# Task view
def task(request):
    pass
    return render(request, 'taskmanager/test.html', locals())
