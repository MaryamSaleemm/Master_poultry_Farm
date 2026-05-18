import re
from django.core.exceptions import ValidationError

def validate_phone(value):
    """
    Validates Pakistani phone numbers (e.g., 03001234567 or +923001234567).
    """
    pattern = re.compile(r'^(\+92|0)?3\d{9}$')
    if not pattern.match(value):
        raise ValidationError('Enter a valid phone number (e.g., 03001234567).')

def validate_positive(value):
    """
    Ensures a number is 0 or greater.
    """
    if value < 0:
        raise ValidationError('This value cannot be negative.')

def validate_non_zero(value):
    """
    Ensures a number is strictly greater than 0.
    """
    if value <= 0:
        raise ValidationError('This value must be greater than zero.')