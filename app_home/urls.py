from django.urls import path
from .views import HomeView


app_name = "app_home"

urlpatterns = [
    path("", HomeView.as_view(), name="home_page")
]
