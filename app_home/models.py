from django.db import models


class ReceiveMessage(models.Model):
    fullname = models.CharField(
        max_length   = 255,
        verbose_name = "فرستنده"
    )
    email = models.EmailField(
        max_length   = 255,
        verbose_name = "ایمیل",
    )
    message = models.TextField(
        verbose_name = "پیام"
    )
    date_time = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "تاریخ و زمان"
    )
    read = models.BooleanField(
        default      = False,
        verbose_name = "خوانده شده"
    )

    class Meta:
        verbose_name        = "پیام"
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return str(self.fullname)
