from django import forms
from .models import ReceiveMessage


class ReceiveMessageForm(forms.ModelForm):

    class Meta:
        model  = ReceiveMessage
        fields = ["fullname", "email", "message"]

        widgets = {
            "fullname": forms.TextInput(attrs={
                "type": "text",
                "required": "",
                "placeholder": "نام و نام خانوادگی",
                "class": "col form-control bg-transparent text-white font-17 fw-bold ms-1"
            }),
            "email": forms.TextInput(attrs={
                "type": "email",
                "required": "",
                "placeholder": "ایمیل شما",
                "class": "col form-control bg-transparent text-white font-17 fw-bold me-1"
            }),
            "message": forms.Textarea(attrs={
                "rows": "3",
                "required": "",
                "placeholder": "متن پیام ...",
                "class": "form-control bg-transparent text-white font-17 fw-bold"
            }),
        }