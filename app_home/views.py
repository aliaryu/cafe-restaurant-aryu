from django.shortcuts import render
from django.views.generic import TemplateView
from app_item.models import Category, Item


class HomeView(TemplateView):
    template_name = "app_home/home.html"

    def get_context_data(self, **kwargs):
        context    = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        items      = Item.objects.order_by("-like")[:12]
        context["categories"] = categories
        context["items"]      = items
        return context