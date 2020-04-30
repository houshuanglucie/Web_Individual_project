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


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'description', 'assignee', 'start_date', 'due_date', 'priority', 'status']

        def __init__(self, *args, **kwargs):
            super(EditTaskForm, self).__init__(*args, **kwargs)
            for field_name in self.base_fields:
                field = self.base_fields[field_name]
                field.widget.attrs.update({"class":"form-control"})

