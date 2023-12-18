from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Role, Staff


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    model         = get_user_model()

    ordering      = ("email",)
    search_fields = ("email", "last_name", "phone")
    list_display  = ("email", "phone", "first_name", "last_name", "is_staff")
    fieldsets     = (
        ("اطلاعات یکتا",     {"fields": ("email", "phone")}),
        ("اطلاعات فردی",     {"fields": ("first_name", "last_name", "address")}),
        ("دسترسی ها",       {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("تاریخ های مرتبط", {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("last_login", "date_joined")
    add_fieldsets   = (
        ("اطلاعات یکتا", {"fields": ("email", "phone"),}),
        ("اطلاعات فردی", {"fields": ("first_name", "last_name", "address")}),
        ("دسترسی ها",   {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("رمز عبور",    {"fields": ("password1", "password2"),}),
    )

# admin.site.register(get_user_model(), UserAdmin)

admin.site.register(Role)
admin.site.register(Staff)