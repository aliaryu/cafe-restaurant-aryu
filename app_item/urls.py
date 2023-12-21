from django.urls import path
from .views import ItemDetailVeiw


app_name = "app_item"

urlpatterns = [
    path("item/<int:pk>/", ItemDetailVeiw.as_view(), name="item_detail_page")
]