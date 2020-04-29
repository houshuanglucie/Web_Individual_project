from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from .forms import ConnectionForm
from .models import Project, Task, Journal


# connection view
def connection(request):
    error = False

    form = ConnectionForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            project_list = user.project_set.all()
            return render(request, 'taskmanager/projects.html', locals())
        else:
            error = True

    return render(request, 'taskmanager/login.html', locals())


# disconnection view
def disconnection(request):
    logout(request)
    return render(request, 'taskmanager/login.html', locals())


# # list of projects
# @login_required
# def projects(request, user_id):
#     user = get_object_or_404(Project, id=user_id)
#     project_list = Project.objects.filter(members__contains=user)
#     return render(request, 'taskmanager/projects.html', locals())


# List of tasks in one project
def project(request, project_id):
    project_get = get_object_or_404(Project, id=project_id)
    task_list = Task.objects.filter(project=project_get)
    return render(request, 'taskmanager/project.html', locals())


# Task details view
def task(request, task_id):
    task_get = get_object_or_404(Task, id=task_id)
    journal_list = Journal.objects.filter(task=task_get)
    return render(request, 'taskmanager/task_detail.html', locals())
