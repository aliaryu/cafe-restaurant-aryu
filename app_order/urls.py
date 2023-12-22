from django.urls import path
from .views import CartView


app_name = "app_order"

urlpatterns = [
    path("",         CartView.as_view(), name="cart_page"),
]
