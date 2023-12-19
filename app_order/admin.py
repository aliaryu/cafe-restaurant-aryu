from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model           = OrderItem
    extra           = 0
    fields          = ("item", "get_item_price", "count")
    readonly_fields = ("get_item_price", )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model           = Order
    inlines         = (OrderItemInline,)
    ordering        = ("-date_time", "-is_complete")
    search_fields   = ("pk", "user__last_name", "user__phone", "get_user_fullname")
    list_display    = ("__str__", "user", "get_user_fullname", "date_time", "in_process", "is_complete", "staff")
    fieldsets       = (
        ("اطلاعات مشتری", {"fields": ("user", "get_user_fullname", "get_user_phone", "get_user_address")}),
        ("اطلاعات سفارش", {"fields": ("staff", "date_time", "in_process", "is_complete", "get_total_cost")}),
    )
    readonly_fields = ("date_time", "user", "get_user_fullname", "get_user_phone", "get_user_address", "get_total_cost")

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return ("date_time", "get_user_fullname", "get_user_phone", "get_user_address", "get_total_cost")
        return super().get_readonly_fields(request, obj)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    model           = OrderItem
    ordering        = ("-order__date_time",)
    search_fields   = ("order__id",)
    list_display    = ("item", "order", "get_order_datetime", "count")
    fieldsets       = (
        ("اطلاعات آیتم سفارش شده", {"fields": ("order", "item", "get_order_datetime", "count")}),
    )
    readonly_fields = ("order", "item", "get_order_datetime", "count")
    
    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return ("get_order_datetime",)
        return super().get_readonly_fields(request, obj)