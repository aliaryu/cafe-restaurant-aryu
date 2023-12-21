from django.shortcuts import render, redirect
from django.views.generic import DetailView, View
from .models import Item, ItemComment
from django.db.models import F
from django.db.models import Prefetch


class ItemDetailVeiw(DetailView):
    model               = Item
    template_name       = "app_item/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = Item.objects.select_related("category").prefetch_related(
            Prefetch("itemcomment_set", queryset=ItemComment.objects.filter(approve=True).select_related("user"))
            ).get(pk=self.kwargs.get("pk"))
        return context

        # GOOD QUERY ;p
        # Item.objects.select_related("category").prefetch_related(
        #     Prefetch("itemcomment_set", queryset=ItemComment.objects.filter(approve=True).select_related("user"))
        #     ).get(pk=self.kwargs.get("pk"))


class ItemLikeView(View):
    def get(self, request, pk):
        item = Item.objects.select_related("category").prefetch_related("itemcomment_set").get(pk=self.kwargs.get("pk"))
        item.like = F("like") + 1
        item.save()
        return redirect("app_item:item_detail_page", pk=pk)