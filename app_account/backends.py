from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class EmailOrPhoneModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_model().objects.get(Q(email=username) | Q(phone=username))

        if user and user.check_password(password):
            return user
        return None
