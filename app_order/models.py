from django.db import models
from django.core.exceptions import ValidationError


class Order(models.Model):
    item = models.ManyToManyField(
        to           = "app_item.Item",
         through     = "OrderItem",
        verbose_name = "آیتم ها"
    )
    user = models.ForeignKey(
        to           = "app_account.User",
        on_delete    = models.SET_NULL,
        null         = True,
        verbose_name = "کاربر"
    )
    staff = models.ForeignKey(
        to           = "app_account.Staff",
        on_delete    = models.SET_NULL,
        null         = True,
        blank        = True,
        default      = None,
        verbose_name = "کارمند"
    )
    date_time = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "تاریخ و زمان"
    )
    in_process  = models.BooleanField(
        default      = False,
        verbose_name = "در حال انجام"
    )
    is_complete = models.BooleanField(
        default = False,
        verbose_name = "تکمیل شده"
    )

    class Meta:
        verbose_name        = "سفارش"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return f"سفارش شماره  [ {self.id} ]"


class OrderItem(models.Model):
    order = models.ForeignKey(
        to           = "Order",
        on_delete    = models.CASCADE,
        verbose_name = "سفارش"
    )
    item = models.ForeignKey(
        to           = "app_item.Item",
        on_delete    = models.CASCADE,
        verbose_name = "آیتم"
    )
    count = models.PositiveIntegerField(
        verbose_name = "تعداد"
    )

    class Meta:
        verbose_name        = "آیتم سفارش شده"
        verbose_name_plural = "آیتم های سفارش شده"

    def __str__(self):
        return f"آیتم [ {self.item} ] تعداد: {self.count}"
