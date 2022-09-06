import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def contains_uppercase(password: str) -> None:
    if not re.search("[A-Z]", password):
        raise ValidationError(
            _("This field must contain at least one uppercase letter")
        )


def contains_lowercase(password: str) -> None:
    if not re.search("[a-z]", password):
        raise ValidationError(
            _("This field must contain at least one lower letter")
        )


def contains_digits(password: str) -> None:
    if not re.search(r"\d", password):
        raise ValidationError(
            _("This field must contain at least one digit")
        )


def contains_special_symbols(password: str) -> None:
    if not re.search(r"[!@#$%^&*\-_=+.,]", password):
        raise ValidationError(
            _("This field must contain at least one special character like: ! @ # $ % ^ & * _ + =")
        )
