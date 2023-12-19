from django.db import models
from django.core.exceptions import ValidationError


class Order(models.Model):
    item = models.ManyToManyField(
        to           = "app_item.Item",
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
        default = False
    )
    is_complete = models.BooleanField(
        default = False
    )

    class Meta:
        verbose_name        = "سفارش"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return f'سفارش شماره "{self.id}"'


