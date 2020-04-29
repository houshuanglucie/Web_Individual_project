from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=300, verbose_name="project name")
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=220, verbose_name="task status")

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name="project")
    name = models.CharField(max_length=300, verbose_name="name")
    description = models.CharField(max_length=300, verbose_name="description")
    assignee = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="assignee")
    start_date = models.DateField(null=True, verbose_name="start_date")
    due_date = models.DateField(null=True, verbose_name="due_date")
    priority = models.IntegerField(verbose_name="priority")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name="status")

    def __str__(self):
        return self.name


class Journal(models.Model):
    date = models.DateField(null=True, verbose_name="date")
    entry = models.CharField(max_length=300, verbose_name="entry")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="author")
    task = models.ForeignKey('Task', on_delete=models.CASCADE, verbose_name="task")

    def __str__(self):
        return self.entry

