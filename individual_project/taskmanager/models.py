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
    name = models.CharField(max_length=300, verbose_name="task name")
    description = models.CharField(max_length=300, verbose_name="task description")
    assignee = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="task assignee")
    start_date = models.DateField(null=True, verbose_name="task start time")
    due_date = models.DateField(null=True, verbose_name="task due time")
    priority = models.IntegerField()
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name="task status")

    def __str__(self):
        return self.name


class Journal(models.Model):
    date = models.DateField(null=True)
    entry = models.CharField(max_length=300)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)

    def __str__(self):
        return self.entry

