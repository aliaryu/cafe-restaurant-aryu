from django.shortcuts import render
from django.views.generic import DetailView
from .models import Item


class ItemDetailVeiw(DetailView):
    model               = Item
    template_name       = "app_item/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = Item.objects.select_related("category").prefetch_related("itemcomment_set").get(pk=self.kwargs.get("pk"))
        return context