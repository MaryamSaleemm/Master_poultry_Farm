import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone(value):
    """
    Validates Pakistani phone numbers (e.g., 03001234567 or +923001234567).
    """
    pattern = re.compile(r'^(\+92|0)?3\d{9}$')
    if not pattern.match(value):
        raise ValidationError(_('Enter a valid phone number (e.g., 03001234567).'))

def validate_construction_year(value):
    """
    Ensures construction year is reasonable (e.g., between 1900 and 2100).
    """
    if value < 1900 or value > 2100:
        raise ValidationError(_('Enter a valid 4-digit year (e.g., 2020).'))