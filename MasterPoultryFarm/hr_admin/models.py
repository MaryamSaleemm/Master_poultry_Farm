from django.db import models
from django.utils import timezone


class OwnerAddress(models.Model):
    """Stores addresses for Owners/Employees"""
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.street}, {self.city}"

class Branches(models.Model):
    """Farm Branches/Locations"""
    branch_name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.branch_name


class EmployeeBasic(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=50, unique=True)
    dob = models.DateField(verbose_name="Date of Birth")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmployeeContact(models.Model):
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    address = models.ForeignKey(OwnerAddress, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Contact: {self.employee}"

class EmployeeAccess(models.Model):
    ROLES = [('Admin', 'Admin'), ('HR', 'HR'), ('Employee', 'Employee'), ('Manager', 'Manager')]
    
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    user_role = models.CharField(max_length=20, choices=ROLES)
    access_level = models.IntegerField(default=1)
    rfid_card_number = models.CharField(max_length=80, blank=True, null=True)

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

    def __str__(self):
        return f"{self.job_title} - {self.employee}"

class Promotions(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    promotion_date = models.DateField()
    old_job_title = models.CharField(max_length=100)
    new_job_title = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

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


class EmployeePayroll(models.Model):
    SALARY_TYPE = [('Hourly', 'Hourly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')]

    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    salary_type = models.CharField(max_length=20, choices=SALARY_TYPE)
    base_salary = models.DecimalField(max_digits=12, decimal_places=2)
    pay_grade = models.CharField(max_length=50)
    bonus_eligible = models.BooleanField(default=False)

class EmployeeBank(models.Model):
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=80)
    iban = models.CharField(max_length=50)

class EmployeeTax(models.Model):
    employee = models.OneToOneField(EmployeeBasic, on_delete=models.CASCADE)
    tax_number = models.CharField(max_length=80)
    tax_region = models.CharField(max_length=100)

class EmployeeInsurance(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=150)
    policy_number = models.CharField(max_length=80)
    coverage_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


class EmployeeAttendance(models.Model):
    STATUS = [('Present', 'Present'), ('Absent', 'Absent'), ('Half-day', 'Half-day'), ('Remote', 'Remote')]

    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS)

class EmployeePerformance(models.Model):
    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2, help_text="Score out of 100")
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

    def __str__(self):
        return self.program_name

class EmployeeTrainingRecords(models.Model):
    STATUS = [('Completed', 'Completed'), ('In Progress', 'In Progress'), ('Not Started', 'Not Started')]

    employee = models.ForeignKey(EmployeeBasic, on_delete=models.CASCADE)
    training_program = models.ForeignKey(EmployeeTrainingPrograms, on_delete=models.CASCADE)
    enroll_date = models.DateField()
    completion_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS)