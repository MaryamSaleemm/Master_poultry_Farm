import re
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_cnic(value):
    if not value.isdigit():
        raise ValidationError('CNIC must contain only numbers.')
    if len(value) != 13:
        raise ValidationError('CNIC must be exactly 13 digits long.')

def validate_phone(value):
    pattern = re.compile(r'^(\+92|0)?3\d{9}$')
    if not pattern.match(value):
        raise ValidationError('Enter a valid phone number (e.g., 03001234567).')

def validate_rfid(value):
    if len(value) != 10:
        raise ValidationError('RFID number must be exactly 10 characters.')
    if not re.match(r'^[0-9A-Fa-f]+$', value):
        raise ValidationError('RFID must contain only Hex characters (0-9, A-F). No symbols.')

def validate_pk_iban(value):
    value = value.upper().replace(' ', '')
    if len(value) != 24:
        raise ValidationError(f'Pakistan IBAN must be 24 characters. You entered {len(value)}.')
    if not value.startswith('PK'):
        raise ValidationError('Pakistan IBAN must start with "PK".')
    if not value.isalnum():
        raise ValidationError('IBAN must contain only letters and numbers.')

def validate_account_number(value):
    if not value.isdigit():
        raise ValidationError('Account number must contain only digits.')
    if len(value) < 14 or len(value) > 16:
        raise ValidationError('Local account number should be between 14 and 16 digits.')

# Models

class TaxRegion(models.Model):
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    tax_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.city}, {self.province}"

class OwnerAddress(models.Model):
    country = models.CharField(max_length=100, default="Pakistan")
    state_province = models.CharField(max_length=100, verbose_name="Province/State")
    city = models.CharField(max_length=100)
    town_area = models.CharField(max_length=150, verbose_name="Town/Area")
    street = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20, blank=True)
    is_rural_area = models.BooleanField(default=False, verbose_name="Is Rural Area?")
    rural_landmark = models.CharField(max_length=255, blank=True, null=True)

    def clean(self):
        if self.is_rural_area and not self.rural_landmark:
            raise ValidationError("Please provide a landmark for rural areas.")
    class Meta:
        verbose_name = "Owner Address"
        verbose_name_plural = "Owner Address"
    
    def __str__(self):
        return f"{self.street}, {self.city}"

class Branches(models.Model):
    branch_name = models.CharField(max_length=150)
    class Meta:
        verbose_name = "Branches"
        verbose_name_plural = "Branches"
    
    def __str__(self):
        return self.branch_name

class EmployeeBasic(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    national_id = models.CharField(
        max_length=13, 
        unique=True, 
        validators=[validate_cnic],
        verbose_name="CNIC",
        help_text="13 digits without dashes"
    )
    
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.national_id and len(self.national_id) == 13 and self.national_id.isdigit():
            last_digit = int(self.national_id[-1])
            self.gender = 'F' if last_digit % 2 == 0 else 'M'
        
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super(EmployeeBasic, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmployeeContact(models.Model):
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, validators=[validate_phone], unique=True)
    email = models.EmailField(max_length=150, unique=True)
    address = models.ForeignKey(OwnerAddress, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Contact: {self.employee}"

class EmployeeAccess(models.Model):
    ROLES = [('Admin', 'Admin'), ('HR', 'HR'), ('Employee', 'Employee'), ('Manager', 'Manager')]
    
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    user_role = models.CharField(max_length=20, choices=ROLES)
    access_level = models.IntegerField(default=1)
    
    rfid_card_number = models.CharField(
        max_length=10, 
        blank=True, 
        null=True, 
        unique=True, 
        validators=[validate_rfid],
        help_text="Exactly 10 Hex characters (0-9, A-F)"
    )
    
    class Meta:
        verbose_name = "Access"
        verbose_name_plural = "Access"

    def __str__(self):
        return self.username

class EmployeeJob(models.Model):
    EMP_TYPE = [('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Intern', 'Intern')]
    LOC_TYPE = [('Branch', 'Branch'), ('Remote', 'Remote'), ('Hybrid', 'Hybrid')]
    STATUS = [('Active', 'Active'), ('On Leave', 'On Leave'), ('Terminated', 'Terminated'), ('Retired', 'Retired')]

    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, null=True, blank=True)
    manager = models.ForeignKey(EmployeeBasic, related_name='subordinates', on_delete=models.SET_NULL, null=True, blank=True)
    hire_date = models.DateField()
    employment_type = models.CharField(max_length=20, choices=EMP_TYPE)
    work_location = models.CharField(max_length=20, choices=LOC_TYPE)
    status = models.CharField(max_length=20, choices=STATUS)

class EmployeeBank(models.Model):
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=150)
    
    account_number = models.CharField(
        max_length=20, 
        unique=True, 
        validators=[validate_account_number],
        help_text="14-16 Digits"
    )
    
    iban = models.CharField(
        max_length=24, 
        unique=True, 
        validators=[validate_pk_iban],
        help_text="PKxx... (Total 24 chars)"
    )

class EmployeePayroll(models.Model):
    SALARY_TYPE = [('Hourly', 'Hourly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')]
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    salary_type = models.CharField(max_length=20, choices=SALARY_TYPE)
    base_salary = models.DecimalField(max_digits=12, decimal_places=2)
    pay_grade = models.CharField(max_length=50)
    bonus_eligible = models.BooleanField(default=False)

class EmployeeTax(models.Model):
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE)
    tax_number = models.CharField(max_length=80)
    tax_region = models.ForeignKey(TaxRegion, on_delete=models.SET_NULL, null=True)

class EmployeeAttendance(models.Model):
    STATUS = [('Present', 'Present'), ('Absent', 'Absent'), ('Half-day', 'Half-day'), ('Remote', 'Remote')]

    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS)

    def clean(self):
        if self.check_in and self.check_out:
            if self.check_out <= self.check_in:
                raise ValidationError("Check-out time cannot be before or the same as Check-in time.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(EmployeeAttendance, self).save(*args, **kwargs)

class Promotions(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    promotion_date = models.DateField()
    old_job_title = models.CharField(max_length=100)
    new_job_title = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotion"
class EmployeeHistory(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    change_date = models.DateTimeField(default=timezone.now)
    field_changed = models.CharField(max_length=100)
    old_value = models.TextField()
    new_value = models.TextField()
    changed_by = models.ForeignKey(EmployeeBasic, related_name='changes_made', on_delete=models.SET_NULL, null=True)

class EmployeeTermination(models.Model):
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE)
    termination_date = models.DateField()
    reason = models.TextField()
    exit_interview_notes = models.TextField(blank=True)

class EmployeeInsurance(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=150)
    policy_number = models.CharField(max_length=80)
    coverage_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class EmployeePerformance(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField()

class EmployeeLeave(models.Model):
    STATUS = [('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')]
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    approver = models.ForeignKey(EmployeeBasic, related_name='leaves_approved', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS)

class EmployeeTrainingPrograms(models.Model):
    program_name = models.CharField(max_length=150)
    provider = models.CharField(max_length=150)
    duration_days = models.IntegerField()
    def __str__(self): return self.program_name

class EmployeeTrainingRecords(models.Model):
    STATUS = [('Completed', 'Completed'), ('In Progress', 'In Progress'), ('Not Started', 'Not Started')]
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    training_program = models.ForeignKey(EmployeeTrainingPrograms, on_delete=models.CASCADE)
    enroll_date = models.DateField()
    completion_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS)
    
class ToDoItem(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   
    