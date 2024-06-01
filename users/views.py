from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from allauth.account.views import PasswordChangeView

from .forms import CustomUserChangeForm

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('my-account')

class MyAccountPageView(UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user

@login_required
def account(request):
    print("Account view called")
    return render(request, 'account.html')

    return render(request, 'account.html')
