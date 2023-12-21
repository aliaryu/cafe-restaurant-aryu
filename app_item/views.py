from django.shortcuts import render, redirect
from django.views.generic import DetailView, View
from .models import Item, ItemComment
from django.db.models import F
from django.db.models import Prefetch
from .forms import ItemCommentForm


class ItemDetailVeiw(DetailView):
    model               = Item
    template_name       = "app_item/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = Item.objects.select_related("category").prefetch_related(
            Prefetch("itemcomment_set", queryset=ItemComment.objects.filter(approve=True).select_related("user"))
            ).get(pk=self.kwargs.get("pk"))
        context["form"] = ItemCommentForm()
        return context

        # GOOD QUERY ;p
        # Item.objects.select_related("category").prefetch_related(
        #     Prefetch("itemcomment_set", queryset=ItemComment.objects.filter(approve=True).select_related("user"))
        #     ).get(pk=self.kwargs.get("pk"))

    def post(self, request, *args, **kwargs):
        form = ItemCommentForm(request.POST)
        if form.is_valid():
            item_instance         = self.get_object()
            comment_instance      = form.save(commit=False)
            comment_instance.item = item_instance
            comment_instance.user = request.user
            comment_instance.save()
            return redirect('app_item:item_detail_page', pk=item_instance.pk)
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)


class ItemLikeView(View):
    def get(self, request, pk):
        item = Item.objects.select_related("category").prefetch_related("itemcomment_set").get(pk=self.kwargs.get("pk"))
        item.like = F("like") + 1
        item.save()
        return redirect("app_item:item_detail_page", pk=pk)