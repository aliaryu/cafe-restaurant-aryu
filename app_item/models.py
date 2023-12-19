from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length   = 255,
        verbose_name = "دسته بندی"
    )
    image = models.ImageField(
        upload_to    = "category_images/",
        verbose_name = "عکس"
    )

    class Meta:
        verbose_name        = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return str(self.category_name)





