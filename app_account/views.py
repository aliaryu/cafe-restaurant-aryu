from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import LoginForm, SignUpForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from app_order.models import Order


def is_not_authenticated(user):
    return not user.is_authenticated


@method_decorator(user_passes_test(is_not_authenticated, login_url=reverse_lazy("app_home:home_page")), name="dispatch")
class LoginView(LoginView):
    form_class    = LoginForm
    template_name = "app_account/login.html"

    def get_success_url(self):
        return self.request.GET.get("next", reverse_lazy("app_home:home_page"))


@method_decorator(user_passes_test(is_not_authenticated, login_url=reverse_lazy("app_home:home_page")), name="dispatch")
class SignUpView(CreateView):
    template_name = "app_account/signup.html"
    form_class    = SignUpForm

    def get_success_url(self):
        return reverse_lazy("app_home:home_page")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("app_home:home_page")



@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model               = get_user_model()
    template_name       = "app_account/profile.html"
    context_object_name = "profile"
    form_class          = CustomUserChangeForm

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context           = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.filter(user=self.request.user)
        context["form"]   = self.form_class(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("app_account:profile_page")
        else:
            return render(request, self.template_name, {'form': form, 'orders': Order.objects.filter(user=self.request.user)})
