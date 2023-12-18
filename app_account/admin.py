from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role, Staff


class StaffInline(admin.StackedInline):
    model = Staff
    verbose_name= "اطلاعات کارمند"


@admin.register(User)
class UserAdmin(UserAdmin):
    model         = User
    inlines       = (StaffInline,)
    ordering      = ("email",)
    search_fields = ("email", "last_name", "phone")
    list_display  = ("email", "phone", "first_name", "last_name", "is_staff")
    fieldsets     = (
        ("اطلاعات یکتا",     {"fields": ("email", "phone")}),
        ("اطلاعات فردی",     {"fields": ("first_name", "last_name", "address")}),
        ("سطح دسترسی",      {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("گروه - اجازه ها", {"fields": ("groups", "user_permissions")}),
        ("تاریخ های مرتبط", {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("last_login", "date_joined")
    add_fieldsets   = (
        ("اطلاعات یکتا", {"fields": ("email", "phone"),}),
        ("اطلاعات فردی", {"fields": ("first_name", "last_name", "address")}),
        ("دسترسی ها",   {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("رمز عبور",    {"fields": ("password1", "password2"),}),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    model         = Role
    search_fields = ("role_name",)
    list_display  = ("role_name", "salary")
    fieldsets     = (
        ("اطلاعات مسئولیت", {"fields": ("role_name", "salary")}),
    )
    add_fieldsets = (
        ("اطلاعات مسئولیت", {"fields": ("role_name", "salary")}),
    )


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    model         = Staff
    list_display  = ("user", "role", "user_first_name", "user_last_name", "user_salary")
    fieldsets     = (
        ("اطلاعات کارمند", {"fields": ("user", "role")}),
    )
    add_fieldsets = (
        ("اطلاعات مسئولیت", {"fields": ("user", "role")}),
    )

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name
    
    def user_salary(self, obj):
        return obj.role.salary

    user_first_name.short_description = "نام"
    user_last_name.short_description  = "نام خانوادگی"
    user_salary.short_description     = "حقوق"
