import re
from django.core.exceptions import ValidationError

def validate_cnic(value):
    """
    Validates Pakistani CNIC: 
    - Exactly 13 digits.
    - Numeric only.
    """
    if not value.isdigit():
        raise ValidationError('CNIC must contain only numbers.')
    if len(value) != 13:
        raise ValidationError('CNIC must be exactly 13 digits long.')

def validate_phone(value):
    """
    Validates phone numbers. Accepts +92 or 03xx formats.
    """
    pattern = re.compile(r'^(\+92|0)?3\d{9}$')
    if not pattern.match(value):
        raise ValidationError('Enter a valid phone number (e.g., 03001234567).')

def validate_rfid(value):
    """
    Strict RFID Validation:
    - Fixed length: 10 characters.
    - Hexadecimal only (0-9, A-F).
    """
    if len(value) != 10:
        raise ValidationError('RFID number must be exactly 10 characters.')
    
    if not re.match(r'^[0-9A-Fa-f]+$', value):
        raise ValidationError('RFID must contain only Hex characters (0-9, A-F). No symbols.')

def validate_pk_iban(value):
    """
    Strict Pakistan IBAN Validation:
    - Starts with 'PK'.
    - Exactly 24 characters.
    - Alphanumeric.
    """
    value = value.upper().replace(' ', '')
    
    if len(value) != 24:
        raise ValidationError(f'Pakistan IBAN must be 24 characters. You entered {len(value)}.')
    
    if not value.startswith('PK'):
        raise ValidationError('Pakistan IBAN must start with "PK".')
    
    if not value.isalnum():
        raise ValidationError('IBAN must contain only letters and numbers.')

def validate_account_number(value):
    """
    Local Bank Account: 14-16 digits usually.
    """
    if not value.isdigit():
        raise ValidationError('Account number must contain only digits.')
    if len(value) < 14 or len(value) > 16:
        raise ValidationError('Local account number should be between 14 and 16 digits.')