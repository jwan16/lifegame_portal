from django.contrib.auth.forms import AuthenticationForm

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user username', 
            'placeholder': 'Account Name', 
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form_control-user password',
            'id': 'passwordBox',
        }
))