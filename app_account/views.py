from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


def is_not_authenticated(user):
    return not user.is_authenticated

@method_decorator(user_passes_test(is_not_authenticated, login_url=reverse_lazy("home_page")), name='dispatch')
class LoginView(LoginView):
    form_class = LoginForm
    template_name = "app_account/login.html"

    def get_success_url(self):
        return reverse_lazy("home_page")
