from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator



phone_numeric_validator = RegexValidator(
    regex   = r"^\d+$",
    message = "شماره تلفن فقط میتواند شامل اعداد باشد."
)

phone_format_validator = RegexValidator(
    regex   = r"^09\d{9}$",
    message = "شماره تلفن وارد شده باید با 09 شروع شود و 11 رقم باشد.",
)

min_length_validator = MinLengthValidator(
    limit_value = 5,
    message     = "این فیلد نمیتواند کمتر از 5 کاراکتر باشد.",
)