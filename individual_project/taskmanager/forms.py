from django import forms
from .models import Journal, Task


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        exclude = ['task']
        fields = ['date', 'entry', 'author']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['project']
        fields = ['name', 'description', 'assignee', 'start_date', 'due_date', 'priority', 'status']
