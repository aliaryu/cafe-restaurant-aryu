from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from app_item.models import Item
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json

@method_decorator(login_required, name='post')
class CartView(ListView):
    template_name       = "app_order/cart.html"
    context_object_name = "items"

    def get_queryset(self):
        cookies = self.request.COOKIES.get("cart")
        cookies = json.loads(cookies) if isinstance(cookies, str) else {}
        items   = Item.objects.filter(id__in=list(cookies.keys()))
        return items
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        output  = []
        cookies = self.request.COOKIES.get("cart")
        cookies = json.loads(cookies) if isinstance(cookies, str) else {}
        for item in context["items"]:
            output.append([item, cookies[str(item.id)]])
        context["items"] = output
        return context

    def post(self, request):
        cookies = self.request.COOKIES.get("cart")
        cookies = json.loads(cookies) if isinstance(cookies, str) else {}

        if cookies:
            order = Order(user=request.user)
            order.save()
            items  = Item.objects.filter(id__in=list(cookies.keys()))
            for key, value in cookies.items():
                OrderItem.objects.create(order=order, item=items.get(id=int(key)), count=int(value))
            response = redirect("app_home:home_page")
            response.delete_cookie("cart")
            return response
        else:
            return redirect("app_item:order_page")



