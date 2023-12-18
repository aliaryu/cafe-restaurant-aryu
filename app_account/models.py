from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractUser
from .validators import phone_numeric_validator, phone_format_validator, min_length_validator


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(**extra_fields)
    

class User(AbstractUser):
    username = None

    email = models.EmailField(
        max_length   = 255,
        unique       = True,
        verbose_name = "ایمیل",
    )
    phone = models.CharField(
        max_length = 11,
        unique     = True,
        validators = [
            phone_numeric_validator,
            phone_format_validator,
        ],
        verbose_name = "شماره تلفن",
    )
    address = models.CharField(
        max_length = 255,
        validators = [
            min_length_validator,
        ],
        verbose_name = "آدرس",
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "first_name", "last_name"]

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return str(self.email)
