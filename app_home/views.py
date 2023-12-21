from django.shortcuts import render
from django.views.generic import TemplateView
from app_item.models import Category, Item
from .forms import ReceiveMessageForm
from django.contrib import messages


class HomeView(TemplateView):
    template_name = "app_home/home.html"

    def get_context_data(self, **kwargs):
        context    = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        items      = Item.objects.order_by("-like")[:12]
        context["categories"] = categories
        context["items"]      = items
        context["form"]      = ReceiveMessageForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ReceiveMessageForm(request.POST)
        if form.is_valid():
            instance = form.save()
            context = self.get_context_data()
            return render(request, self.template_name, context)

        context = self.get_context_data()
        context["form"] = form
        return render(request, self.template_name, context)
