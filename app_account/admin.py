from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Role, Staff


class UserAdmin(UserAdmin):

    model = get_user_model()
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2'),
        }),
    )

admin.site.register(get_user_model(), UserAdmin)

admin.site.register(Role)
admin.site.register(Staff)