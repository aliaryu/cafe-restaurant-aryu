from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    category_name = models.CharField(
        max_length   = 255,
        unique       = True,
        verbose_name = "دسته بندی"
    )
    image = models.ImageField(
        upload_to    = "category_images/",
        verbose_name = "تصویر"
    )

    def clean(self):
        super().clean()
        if self.image:
            width, height = self.image.width, self.image.height
            if width != height:
                raise ValidationError({"image": "عکس باید مربع باشد. عرض و ارتفاع یکسانی داشته باشد."})

    class Meta:
        verbose_name        = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return str(self.category_name)


class Item(models.Model):
    item_name = models.CharField(
        max_length   = 255,
        unique       = True,
        verbose_name = "آیتم"
    )
    description = models.TextField(
        verbose_name = "توضیحات",
    )
    category  = models.ForeignKey(
        to           = "Category",
        on_delete    = models.SET_NULL,
        null         = True,
        verbose_name = "دسته بندی"
    )
    price = models.DecimalField(
        max_digits     = 10,
        decimal_places = 2,
        verbose_name   = "قیمت",
    )
    count = models.PositiveIntegerField(
        verbose_name = "تعداد",
    )
    image = models.ImageField(
        upload_to    = "item_images/",
        verbose_name = "تصویر"
    )

    class Meta:
        verbose_name        = "آیتم"
        verbose_name_plural = "آیتم ها"

    def __str__(self):
        return str(self.item_name)
    

class ItemComment(models.Model):
    message = models.TextField(
        verbose_name = "پیام"
    )
    date_time = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "تاریخ و زمان"
    )
    answer = models.TextField(
        verbose_name = "پاسخ"
    )
    user = models.ForeignKey(
        to           = "app_account.User",
        on_delete    = models.CASCADE,
        verbose_name = "کاربر",
    )
    item = models.ForeignKey(
        to           = "Item",
        on_delete    = models.CASCADE,
        verbose_name = "آیتم",
    )

    class Meta:
        verbose_name        = "نظر"
        verbose_name_plural = "نظر ها"

    def __str__(self):
        return str(self.user.get_full_name())
