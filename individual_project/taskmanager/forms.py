from django import forms
from .models import Journal, Task


# Form for journal
class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        exclude = ['task']
        fields = ['date', 'entry', 'author']


# Form for task
class TaskForm(forms.ModelForm):
    # Set the default date format "aaaa-mm-jj"
    start_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "aaaa-mm-jj",
                "class": 'form-control'
            }
        )
    )

    # Set the default date format "aaaa-mm-jj"
    due_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "aaaa-mm-jj",
                "class": 'form-control'
            }
        )
    )

    class Meta:
        model = Task
        exclude = ['project']
        fields = ['name', 'description', 'assignee', 'start_date', 'due_date', 'priority', 'status']
