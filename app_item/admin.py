from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Category, Item, ItemComment
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model           = Category
    list_display    = ("category_name", "display_image")
    readonly_fields = ("display_image",)
    fieldsets       = (
        ("اطلاعات دسته بندی", {"fields": ("category_name",)}),
        ("عکس دسته بندی", {"fields": ("display_image", "image",)}),
    )

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="background-color: #121212;"/>'.format(obj.image.url))

    display_image.short_description = "تصویر موجود"


class ItemCommentNotApprovedInline(admin.StackedInline):
    model               = ItemComment
    verbose_name        = "نظر"
    verbose_name_plural = "نظرات تایید نشده"
    classes             = ('collapse',)
    readonly_fields     = ("user", "date_time")
    fieldsets           = (
        (None, {"fields": ("message", "approve", "answer", "user", "date_time")}),
    )
    extra = 0

    def get_queryset(self, request):
        return super().get_queryset(request).filter(approve=False)
    
    # def has_add_permission(self, request, obj=None):
    #     return False


class ItemCommentApprovedInline(admin.StackedInline):
    model               = ItemComment
    verbose_name        = "نظر"
    verbose_name_plural = "نظرات تایید شده"
    classes             = ('collapse',)
    readonly_fields     = ("user", "date_time")
    fieldsets           = (
        (None, {"fields": ("message", "approve", "answer", "user", "date_time")}),
    )
    extra = 0

    def get_queryset(self, request):
        return super().get_queryset(request).filter(approve=True)
    
    # def has_add_permission(self, request, obj=None):
    #     return False


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model           = Item
    inlines         = (ItemCommentNotApprovedInline, ItemCommentApprovedInline)
    list_display    = ("item_name", "price", "count", "display_image")
    readonly_fields = ("display_image",)
    fieldsets       = (
        ("اطلاعات آیتم", {"fields": ("item_name", "price", "count", "description")}),
        ("عکس دسته بندی", {"fields": ("display_image", "image",)}),
    )

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="background-color: #121212;"/>'.format(obj.image.url))

    display_image.short_description = "تصویر موجود"


admin.site.register(ItemComment)