import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone(value):
    pattern = re.compile(r'^(\+92|0)?3\d{9}$')
    if not pattern.match(value):
        raise ValidationError(_('Enter a valid phone number (e.g., 03001234567).'))

def validate_construction_year(value):
    if value < 1900 or value > 2100:
        raise ValidationError(_('Enter a valid 4-digit year (e.g., 2020).'))

# Owner and Structure Tables

class OwnerBasic(models.Model):
    owner_name = models.CharField(max_length=150, unique=True)
    
    class Meta:
        verbose_name_plural = "Owner Basics"

    def clean(self):
        if OwnerBasic.objects.filter(owner_name__iexact=self.owner_name).exclude(pk=self.pk).exists():
            raise ValidationError({'owner_name': f"Owner '{self.owner_name}' already exists."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(OwnerBasic, self).save(*args, **kwargs)

    def __str__(self):
        return self.owner_name

class OwnerContact(models.Model):
    owner = models.ForeignKey(OwnerBasic, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, validators=[validate_phone], help_text="Format: 03001234567")
    email = models.EmailField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = "Owner Contacts"

    def __str__(self):
        return f"{self.owner} - {self.phone}"

class OwnerAddress(models.Model):
    owner = models.ForeignKey(OwnerBasic, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Owner Addresses"

# Building Core Tables

class BuildingBasic(models.Model):
    building_name = models.CharField(max_length=150)
    building_code = models.CharField(max_length=60, unique=True, help_text="Unique Identifier (e.g., BLD-001)")

    class Meta:
        verbose_name_plural = "Building Basics"

    def clean(self):
        if BuildingBasic.objects.filter(building_code__iexact=self.building_code).exclude(pk=self.pk).exists():
            raise ValidationError({'building_code': f"Building Code '{self.building_code}' is already taken."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(BuildingBasic, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.building_name} ({self.building_code})"

class BuildingLocation(models.Model):
    building = models.ForeignKey(BuildingBasic, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Building Locations"

class BuildingSpecs(models.Model):
    CONDITIONS = [('New', 'New'), ('Good', 'Good'), ('Needs Renovation', 'Needs Renovation')]
    STATUS = [('Occupied', 'Occupied'), ('Vacant', 'Vacant'), ('Under Construction', 'Under Construction')]

    building = models.ForeignKey(BuildingBasic, on_delete=models.CASCADE)
    floors = models.IntegerField()
    total_area = models.DecimalField(max_digits=12, decimal_places=2, help_text="Sq Meters")
    construction_year = models.IntegerField(validators=[validate_construction_year], help_text="YYYY Format")
    condition = models.CharField(max_length=20, choices=CONDITIONS)
    occupancy_status = models.CharField(max_length=20, choices=STATUS)

    class Meta:
        verbose_name_plural = "Building Specs"

class BuildingFacilities(models.Model):
    SECURITY = [('CCTV', 'CCTV'), ('Guard', 'Guard'), ('None', 'None'), ('Mixed', 'Mixed')]

    building = models.ForeignKey(BuildingBasic, on_delete=models.CASCADE)
    parking_capacity = models.IntegerField()
    power_backup = models.BooleanField(default=False)
    internet_available = models.BooleanField(default=False)
    security_system = models.CharField(max_length=20, choices=SECURITY)
    additional_notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Building Facilities"

class EmployeeBasic(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    class Meta:
        managed = False 
        db_table = 'hr_admin_employeebasic' 
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BuildingManagement(models.Model):
    building = models.ForeignKey(BuildingBasic, on_delete=models.CASCADE)
    owner = models.ForeignKey(OwnerBasic, on_delete=models.CASCADE)
    manager_employee = models.ForeignKey(EmployeeBasic, on_delete=models.SET_NULL, null=True)
    maintenance_contact = models.CharField(max_length=150)
    emergency_contact = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Building Management"

# Compliance Tables

class Permits(models.Model):
    STATUS = [('Valid', 'Valid'), ('Expired', 'Expired'), ('Revoked', 'Revoked')]

    building = models.ForeignKey(BuildingBasic, on_delete=models.CASCADE)
    permit_type = models.CharField(max_length=150)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS)
    issued_by = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Permits"

class Licenses(models.Model):
    STATUS = [('Valid', 'Valid'), ('Expired', 'Expired'), ('Revoked', 'Revoked')]

    building = models.ForeignKey(BuildingBasic, on_delete=models.CASCADE)
    license_type = models.CharField(max_length=150)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS)

    class Meta:
        verbose_name_plural = "Licenses"

class BuildingInspections(models.Model):
    STATUS = [('Passed', 'Passed'), ('Failed', 'Failed'), ('Follow-up Required', 'Follow-up Required')]

    building = models.ForeignKey(BuildingBasic, on_delete=models.CASCADE)
    inspection_date = models.DateField()
    inspector_name = models.CharField(max_length=150)
    report = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS)

    class Meta:
        verbose_name_plural = "Building Inspections"