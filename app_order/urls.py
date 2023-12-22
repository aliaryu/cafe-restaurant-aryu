from django.urls import path
from .views import CartView, PaymentView


app_name = "app_order"

urlpatterns = [
    path("",         CartView.as_view(), name="cart_page"),
    path("payment/", PaymentView.as_view(), name="payment_url")
]
