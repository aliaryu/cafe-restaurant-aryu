from django import forms
from .models import ItemComment


class ItemCommentForm(forms.ModelForm):

    class Meta:
        model  = ItemComment
        fields = ["message"]

        widgets = {
            "message": forms.Textarea(attrs={
                "rows": "3",
                "required": "",
                "placeholder": "نظر شما ...",
                "class": "form-control bg-transparent text-white font-17 fw-bold"
            }),
        }
