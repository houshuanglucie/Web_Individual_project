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
    # Set the default date format "jj/mm/aaaa"
    start_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "jj/mm/aaaa",
                "class": 'form-control'
            }
        )
    )

    # Set the default date format "jj/mm/aaaa"
    due_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "jj/mm/aaaa",
                "class": 'form-control'
            }
        )
    )

    class Meta:
        model = Task
        exclude = ['project']
        fields = ['name', 'description', 'assignee', 'start_date', 'due_date', 'priority', 'status']
