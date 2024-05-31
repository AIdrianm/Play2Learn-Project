from django.shortcuts import render

# Create your views here.
from allauth.account.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    