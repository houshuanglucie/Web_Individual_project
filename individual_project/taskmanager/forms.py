from django import forms
from .models import Journal, Task


class ConnectionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['date', 'entry', 'author', 'task']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'description', 'assignee', 'start_date', 'due_date', 'priority', 'status']



