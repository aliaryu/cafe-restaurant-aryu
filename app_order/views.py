from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from app_item.models import Item
import json


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


class PaymentView(LoginRequiredMixin, View):
    def get(self, request):
        cookies = self.request.COOKIES.get("cart")
        cookies = json.loads(cookies) if isinstance(cookies, str) else {}

        if cookies:
            
            return redirect("app_home:home_page")
        else:
            return redirect("app_item:order_page")



