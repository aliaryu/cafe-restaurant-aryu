from typing import Any
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields["username"].widget.attrs["class"]       = "form-control bg-transparent text-white font-17 fw-bold"
        self.fields["username"].widget.attrs["placeholder"] = "ایمیل یا شماره تلفن"

        self.fields["password"].widget.attrs["class"]       = "form-control bg-transparent text-white font-17 fw-bold"
        self.fields["password"].widget.attrs["placeholder"] = "رمز عبور"
        