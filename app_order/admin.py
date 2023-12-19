from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model           = OrderItem
    extra           = 0
    fields          = ("item", "available", "count",)
    readonly_fields = ("available",)

    def available(self, obj):
        return obj.item.count
    
    available.short_description = "موجودی"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model           = Order
    inlines         = (OrderItemInline,)
    ordering        = ("-is_complete", "date_time",)
    search_fields   = ("pk", "user__first_name", "user__last_name", "user__phone")
    list_display    = ("__str__", "user", "get_user_fullname", "date_time", "in_process", "is_complete", "staff")
    fieldsets       = (
        ("اطلاعات مشتری", {"fields": ("user", "get_user_fullname", "get_user_phone", "get_user_address")}),
        ("اطلاعات سفارش", {"fields": ("staff", "date_time", "in_process", "is_complete")}),
    )
    readonly_fields = ("date_time", "user", "get_user_fullname", "get_user_phone", "get_user_address")

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return ["date_time", "get_user_fullname", "get_user_phone", "get_user_address"]
        return super().get_readonly_fields(request, obj)










admin.site.register(OrderItem)