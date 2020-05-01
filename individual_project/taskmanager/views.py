from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, JournalForm, TaskForm
from .models import Project, Task, Journal


# list of projects
@login_required
def projects(request):
    project_list = request.user.project_set.all()
    return render(request, 'taskmanager/projects.html', locals())


# List of tasks in one project
@login_required
def project(request, project_id):
    project_get = get_object_or_404(Project, id=project_id)
    task_list = Task.objects.filter(project=project_get)
    return render(request, 'taskmanager/project.html', locals())


# Task details view
@login_required
def task(request, task_id):
    task_get = get_object_or_404(Task, id=task_id)
    journal_list = Journal.objects.filter(task=task_get)
    return render(request, 'taskmanager/task_detail.html', locals())


# Add a new journal of a task
@login_required
def add_journal(request):
    if request.method != 'POST':
        form = JournalForm()
    else:
        new_journal = JournalForm(request.POST)
        if new_journal.is_valid():
            new_journal.save()
            task_get = new_journal.cleaned_data['task']
            journal_list = Journal.objects.filter(task=task_get)
            return render(request, 'taskmanager/task_detail.html', locals())
    return render(request, 'taskmanager/add_journal.html', locals())


# Add a new task of a project
@login_required
def add_task(request):
    edit = False
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            project_get = form.cleaned_data['project']
            task_list = Task.objects.filter(project=project_get)
            return render(request, 'taskmanager/project.html', locals())
    return render(request, 'taskmanager/add_task.html', locals())


# Edit a task
@login_required
def edit_task(request, task_id):
    edit = True
    task_before = Task.objects.get(id=task_id)
    if request.method != 'POST':
        form = TaskForm(instance=task_before)
    else:
        form = TaskForm(data=request.POST, instance=task_before)
        if form.is_valid():
            form.save()
            project_get = form.cleaned_data['project']
            task_list = Task.objects.filter(project=project_get)
            return render(request, 'taskmanager/project.html', locals())
    context = {'form': form, 'task': task_before, 'edit': edit}
    return render(request, 'taskmanager/add_task.html', context)


# Delete a task
# @login_required
# def del_task(request, task_id):
#     delete = True
#     task_current = Task.objects.get(id=task_id)
#     if request.method == 'POST':
#         project_get = task_current.cleaned_data['project']
#         task_current.delete()
#         task_list = Task.objects.filter(project=project_get)
#         return render(request, 'taskmanager/project.html', locals())
#         # return redirect('app1:article')
#     return render(request, 'taskmanager/add_task.html', locals())

