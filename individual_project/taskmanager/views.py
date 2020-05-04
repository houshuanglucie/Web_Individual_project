from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import JournalForm, TaskForm
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
def add_journal(request, task_id):
    task_get = Task.objects.get(id=task_id)
    if request.method != 'POST':
        form = JournalForm()
        form.fields['author'].queryset = task_get.project.members
    else:
        form = JournalForm(request.POST)
        if form.is_valid():
            new_journal = form.save(commit=False)
            new_journal.task = task_get
            new_journal.save()
            journal_list = Journal.objects.filter(task=task_get)
            return render(request, 'taskmanager/task_detail.html', locals())
    return render(request, 'taskmanager/add_journal.html', locals())


# Add a new task of a project
@login_required
def add_task(request, project_id):
    method = 'Add'
    project_get = Project.objects.get(id=project_id)
    if request.method != 'POST':
        form = TaskForm()
        form.fields['assignee'].queryset = project_get.members
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.project = project_get
            form.save()
            task_list = Task.objects.filter(project=project_get)
            return render(request, 'taskmanager/project.html', locals())
    return render(request, 'taskmanager/add_task.html', locals())


# Edit a task
@login_required
def edit_task(request, task_id):
    method = 'Edit'
    task_before = Task.objects.get(id=task_id)
    project_get = task_before.project
    if request.method != 'POST':
        form = TaskForm(instance=task_before)
        form.fields['assignee'].queryset = project_get.members
    else:
        form = TaskForm(data=request.POST, instance=task_before)
        if form.is_valid():
            task_after = form.save(commit=False)
            task_after.project = project_get
            task_after.save()
            task_list = Task.objects.filter(project=project_get)
            return render(request, 'taskmanager/project.html', locals())
    context = {'form': form, 'task': task_before, 'method': method}
    return render(request, 'taskmanager/add_task.html', context)


# Delete a task
@login_required
def del_task(request, task_id):
    task_current = Task.objects.get(id=task_id)
    project_get = task_current.project
    task_current.delete()
    task_list = Task.objects.filter(project=project_get)
    return render(request, 'taskmanager/project.html', locals())

