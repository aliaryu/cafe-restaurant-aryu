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
    description = models.CharField(
        max_length   = 255,
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
    


