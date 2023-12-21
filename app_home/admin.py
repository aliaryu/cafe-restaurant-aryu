from django.contrib import admin
from .models import ReceiveMessage


@admin.register(ReceiveMessage)
class UserAdmin(admin.ModelAdmin):
    model         = ReceiveMessage
    ordering      = ("-date_time",)
    list_display  = ("fullname", "email", "date_time", "read")
    fieldsets     = (
        ("اطلاعات فرستنده", {"fields": ("fullname", "email")}),
        ("اطلاعات پیام",    {"fields": ("message", "date_time")}),
        ("وضعیت خواندن",   {"fields": ("read", )}),
    )
    readonly_fields = ("date_time", )
