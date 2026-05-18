from django.core.exceptions import ValidationError

def validate_positive(value):
    """Ensures a number is 0 or greater."""
    if value < 0:
        raise ValidationError('This value cannot be negative.')

def validate_non_zero(value):
    """Ensures a number is strictly greater than 0."""
    if value <= 0:
        raise ValidationError('This value must be greater than zero.')