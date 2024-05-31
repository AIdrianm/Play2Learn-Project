from allauth.account.forms import LoginForm
from django import forms

class CustomLoginForm(LoginForm):
    login = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        label="Username"
    )
    
    def login(self, *args, **kwargs):
        # Override login method to use username instead of email
        self.cleaned_data['login'] = self.cleaned_data['login'].lower()
        return super().login(*args, **kwargs)
