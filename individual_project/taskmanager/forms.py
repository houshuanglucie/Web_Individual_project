from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
