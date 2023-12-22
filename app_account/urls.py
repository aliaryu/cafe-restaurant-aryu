from django.urls import path
from .views import LoginView, SignUpView, LogoutView, ProfileView


app_name = "app_account"

urlpatterns = [
    path("login/",   LoginView.as_view(),   name="login_page"),
    path("signup/",  SignUpView.as_view(),  name="signup_page"),
    path("logout/",  LogoutView.as_view(),  name="logout_page"),
    path("profile/", ProfileView.as_view(), name="profile_page")
]
