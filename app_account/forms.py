from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-control bg-transparent text-white font-17 fw-bold",
            "placeholder":"ایمیل یا شماره تلفن",
            "type": "email"
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-control bg-transparent text-white font-17 fw-bold",
            "placeholder": "رمز عبور"
        })


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "password1", "password2", "address", "phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "class": "form-control bg-transparent text-white font-17 fw-bold ms-1",
            "placeholder": "نام",
            "required": "",
        })
        self.fields["last_name"].widget.attrs.update({
            "class": "form-control bg-transparent text-white font-17 fw-bold me-1",
            "placeholder": "نام خانوادگی",
            "required": "",
        })
        self.fields["email"].widget.attrs.update({
            "class": "form-control bg-transparent text-white font-17 fw-bold",
            "placeholder": "ایمیل",
            "required": "",
            "type": "email",
        })
        self.fields["password1"].widget.attrs.update({
            "class": "form-control bg-transparent text-white font-17 fw-bold ms-1",
            "placeholder": "رمز عبور",
            "required": "",
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control bg-transparent text-white font-17 fw-bold me-1",
            "placeholder": "تکرار رمز عبور",
            "required": "",
        })
        self.fields["address"] = forms.CharField(
            widget=forms.Textarea(attrs={
                "class": "form-control bg-transparent text-white font-17 fw-bold",
                "placeholder": "آدرس ...",
                "required": "",
                "rows": 3
            })
        )
        self.fields["phone"].widget.attrs.update({
            "class": "form-control bg-transparent text-white font-17 fw-bold",
            "placeholder": "شماره تلفن",
            "required": "",
            "type": "tel"
        })

        self.fields["email"].widget.attrs.pop("autofocus")
