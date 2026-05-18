from django.db import models
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value < 0:
        raise ValidationError('This value cannot be negative.')

def validate_non_zero(value):
    if value <= 0:
        raise ValidationError('This value must be greater than zero.')


class BirdBreeds(models.Model):
    breed_name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=[('Layer','Layer'), ('Broiler','Broiler')])
    
    class Meta:
        verbose_name = "Breeds"
        verbose_name_plural = "Breeds"
    def clean(self):
        if BirdBreeds.objects.filter(breed_name__iexact=self.breed_name).exclude(pk=self.pk).exists():
            raise ValidationError({'breed_name': f"The breed '{self.breed_name}' already exists."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(BirdBreeds, self).save(*args, **kwargs)

    def __str__(self): return self.breed_name

class Batches(models.Model):
    house = models.ForeignKey('farm_infra.Houses', on_delete=models.CASCADE)
    batch_code = models.CharField(max_length=80, unique=True, help_text="Unique Identifier (e.g., BATCH-2025-01)")
    breed = models.ForeignKey(BirdBreeds, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[validate_non_zero])
    arrival_date = models.DateField()

    class Meta:
        verbose_name = "Batches"
        verbose_name_plural = "Batches"
    def clean(self):
        if Batches.objects.filter(batch_code__iexact=self.batch_code).exclude(pk=self.pk).exists():
            raise ValidationError({'batch_code': f"Batch Code '{self.batch_code}' already exists."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Batches, self).save(*args, **kwargs)

    def __str__(self): return self.batch_code

class Vaccines(models.Model):
    vaccine_name = models.CharField(max_length=150, unique=True)
    
    class Meta:
        verbose_name = "Vaccines"
        verbose_name_plural = "Vaccines"
    
    def clean(self):
        if Vaccines.objects.filter(vaccine_name__iexact=self.vaccine_name).exclude(pk=self.pk).exists():
            raise ValidationError({'vaccine_name': "This vaccine already exists."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Vaccines, self).save(*args, **kwargs)

    def __str__(self): return self.vaccine_name

class VaccineRecords(models.Model):
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccines, on_delete=models.CASCADE)
    date_administered = models.DateField()
    dose = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Vaccines Records"
        verbose_name_plural = "Vaccines Records"
class MortalityRecords(models.Model):
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    date = models.DateField()
    count = models.IntegerField(validators=[validate_positive], help_text="Number of birds died")
    cause = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Mortality Records"
        verbose_name_plural = "Mortality Records"
    
class EggCollection(models.Model):
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    date = models.DateField()
    eggs_collected = models.IntegerField(validators=[validate_positive])
    broken = models.IntegerField(default=0, validators=[validate_positive])

class VetVisits(models.Model):
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    visit_date = models.DateField()
    vet_name = models.CharField(max_length=150)
    findings = models.TextField()
    class Meta:
        verbose_name = "Vet Visists"
        verbose_name_plural = "Vet Visits"

class FarmTasks(models.Model):
    task = models.CharField(max_length=255)
    assigned_to = models.ForeignKey('hr_admin.EmployeeBasic', on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending','Pending'), ('Done','Done')])
    
    class Meta:
        verbose_name = "Farm Tasks"
        verbose_name_plural = "Farm Tasks"
        
class FarmStatus(models.Model):
    single_egg_price = models.DecimalField(max_digits=5, decimal_places=2, default=30.00)
    box_price = models.DecimalField(max_digits=10, decimal_places=0, default=10800)
    current_tray_price = models.DecimalField(max_digits=10, decimal_places=0, default=900)

    eggs_in_stock = models.BooleanField(default=True, help_text="Uncheck if Eggs are Sold Out")
    hens_in_stock = models.BooleanField(default=False, help_text="Check if Cull Birds are available for sale")

    class Meta:
        verbose_name_plural = "Daily Rates & Stock"

    def __str__(self):
        return f"Rates (Box: {self.box_price})"