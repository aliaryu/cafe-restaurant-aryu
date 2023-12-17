from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractUser


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
        max_length=255,
        unique=True,
        verbose_name="ایمیل",
    )
    phone = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="تلفن همراه",
    )
    address = models.CharField(
        max_length=255,
        verbose_name="آدرس",
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "first_name", "last_name"]

    def __str__(self):
        return str(self.email)
