from django.urls import path
from .views import ItemDetailVeiw, ItemLikeView


app_name = "app_item"

urlpatterns = [
    path("item/<int:pk>/",      ItemDetailVeiw.as_view(), name="item_detail_page"),
    path("item-like/<int:pk>/", ItemLikeView.as_view(),   name="item_like_url"),
]