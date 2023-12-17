from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.contrib.auth import authenticate, login



class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(
        max_length=255,
        verbose_name="نام",
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="نام خانوادگی",
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="ایمیل",
    )
    phone = models.PositiveBigIntegerField(
        unique=True,
        verbose_name="تلفن همراه",
    )
    address = models.CharField(
        max_length=255,
        verbose_name="آدرس",
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name="کارمند",
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ عضویت",
    )

    groups = models.ManyToManyField(Group, related_name='user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_set', blank=True)

    USERNAME_FIELD = "email"

    def __str__(self):
        return str(self.email)
