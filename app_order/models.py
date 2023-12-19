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
    
    def get_user_fullname(self):
        return f"{self.user.get_full_name()}"
    
    def get_user_phone(self):
        return f"{self.user.phone}"
    
    def get_user_address(self):
        return f"{self.user.address}"
    
    def get_total_cost(self):
        return sum(order_item.item.price * order_item.count for order_item in self.orderitem_set.all())
    
    get_user_fullname.short_description = "نام و نام خانوادگی"
    get_user_phone.short_description    = "شماره تلفن"
    get_user_address.short_description  = "آدرس"
    get_total_cost.short_description    = "قیمت نهایی"


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

    def clean(self):
        super().clean()
        updated_count = self.item.count - self.count
        if updated_count < 0:
            raise ValidationError({"count": "تعداد سفارش بیشتر از موجودی موجود است."})

    def save(self, *args, **kwargs):
        updated_count = self.item.count - self.count
        self.item.count = updated_count
        self.item.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name        = "آیتم سفارش شده"
        verbose_name_plural = "آیتم های سفارش شده"

    def __str__(self):
        return f"آیتم [ {self.item} ] تعداد: {self.count}"

    def get_order_datetime(self):
        return self.order.date_time
    
    def get_item_price(self):
        return self.item.price
    
    get_order_datetime.short_description = "تاریخ و زمان"
    get_item_price.short_description     = "قیمت هر آیتم"