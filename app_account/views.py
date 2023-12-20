from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm, SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.contrib.auth import login


def is_not_authenticated(user):
    return not user.is_authenticated

@method_decorator(user_passes_test(is_not_authenticated, login_url=reverse_lazy("app_home:home_page")), name="dispatch")
class LoginView(LoginView):
    form_class    = LoginForm
    template_name = "app_account/login.html"

    def get_success_url(self):
        return reverse_lazy("app_home:home_page")

@method_decorator(user_passes_test(is_not_authenticated, login_url=reverse_lazy("app_home:home_page")), name="dispatch")
class SignUpView(CreateView):
    template_name = "app_account/signup.html"
    form_class    = SignUpForm

    def get_success_url(self):
        return reverse_lazy("app_account:login_page")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response