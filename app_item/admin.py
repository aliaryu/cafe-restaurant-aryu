from django.contrib import admin
from .models import Category
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
    add_fieldsets   = (
        ("اطلاعات دسته بندی", {"fields": ("category_name",)}),
        ("عکس دسته بندی", {"fields": ("image",)}),
    )

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="background-color: #121212;"/>'.format(obj.image.url))

    display_image.short_description = "تصویر موجود"
