import re
from django.db import models
from django.core.exceptions import ValidationError


def validate_phone(value):
    pattern = re.compile(r'^(\+92|0)?3\d{9}$')
    if not pattern.match(value):
        raise ValidationError('Enter a valid phone number (e.g., 03001234567).')

def validate_positive(value):
    if value < 0:
        raise ValidationError('This value cannot be negative.')

def validate_non_zero(value):
    if value <= 0:
        raise ValidationError('This value must be greater than zero.')

# Models

class FarmBasic(models.Model):
    farm_name = models.CharField(max_length=150, unique=True, help_text="Unique name for the farm")
    description = models.TextField(blank=True)
    
    def clean(self):
        if FarmBasic.objects.filter(farm_name__iexact=self.farm_name).exclude(pk=self.pk).exists():
            raise ValidationError({'farm_name': f"A farm with the name '{self.farm_name}' already exists."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(FarmBasic, self).save(*args, **kwargs)

    def __str__(self): 
        return self.farm_name

class FarmLocation(models.Model):
    farm = models.OneToOneField(FarmBasic, on_delete=models.CASCADE) 
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street_address}, {self.city}"

class FarmOwnership(models.Model):
    farm = models.ForeignKey(FarmBasic, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=150)
    
    owner_contact = models.CharField(
        max_length=15, 
        validators=[validate_phone], 
        help_text="Format: 03001234567"
    )

    class Meta:
        unique_together = ('farm', 'owner_name', 'owner_contact')

    def clean(self):
        if FarmOwnership.objects.filter(
            farm=self.farm, 
            owner_name__iexact=self.owner_name
        ).exclude(pk=self.pk).exists():
            raise ValidationError({
                'owner_name': f"'{self.owner_name}' is already listed as an owner for {self.farm.farm_name}."
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super(FarmOwnership, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.owner_name} - {self.farm}"

class Houses(models.Model):
    TYPES = [('Layer', 'Layer'), ('Broiler', 'Broiler'), ('Breeder', 'Breeder')]
    
    farm = models.ForeignKey(FarmBasic, on_delete=models.CASCADE)
    house_name = models.CharField(max_length=100)
    capacity = models.IntegerField(validators=[validate_non_zero], help_text="Max birds")
    type = models.CharField(max_length=20, choices=TYPES)
    
    class Meta:
        unique_together = ('farm', 'house_name')
        verbose_name_plural = "Houses / Sheds"

    def clean(self):
        if Houses.objects.filter(farm=self.farm, house_name__iexact=self.house_name).exclude(pk=self.pk).exists():
            raise ValidationError({
                'house_name': f"'{self.house_name}' already exists in {self.farm.farm_name}. Please use a different name."
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Houses, self).save(*args, **kwargs)

    def __str__(self): 
        return f"{self.house_name} ({self.farm})"

class HouseSpecs(models.Model):
    house = models.OneToOneField(Houses, on_delete=models.CASCADE)
    floor_area = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])
    ventilation_type = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Houses & Specs"
        verbose_name_plural = "Houses & Specs"
    
    def __str__(self):
        return f"Specs: {self.house}"

class HouseUtilities(models.Model):
    house = models.OneToOneField(Houses, on_delete=models.CASCADE)
    electricity = models.BooleanField(default=True)
    water_source = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Utilities"
        verbose_name_plural = "Utilities"
    
class ConstructionProjects(models.Model):
    farm = models.ForeignKey(FarmBasic, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta:
        verbose_name = "ConstructionProjects"
        verbose_name_plural = "ConstructionProjects"

    def clean(self):
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                raise ValidationError("End Date cannot be before Start Date.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ConstructionProjects, self).save(*args, **kwargs)

    def __str__(self):
        return self.project_name

class FarmAudits(models.Model):
    farm = models.ForeignKey(FarmBasic, on_delete=models.CASCADE)
    audit_date = models.DateField()
    auditor_name = models.CharField(max_length=150)
    report = models.TextField()
    class Meta:
        verbose_name = "Audits"
        verbose_name_plural = "Audits"
    
    def __str__(self):
        return f"Audit {self.audit_date} - {self.farm}"