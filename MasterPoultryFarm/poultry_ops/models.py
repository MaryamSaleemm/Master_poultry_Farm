from django.db import models

class BirdBreeds(models.Model):
    breed_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[('Layer','Layer'), ('Broiler','Broiler')])
    def __str__(self): return self.breed_name

class Batches(models.Model):
    # Links to House in farm_infra
    house = models.ForeignKey('farm_infra.Houses', on_delete=models.CASCADE)
    batch_code = models.CharField(max_length=80)
    breed = models.ForeignKey(BirdBreeds, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    arrival_date = models.DateField()
    def __str__(self): return self.batch_code

class Vaccines(models.Model):
    vaccine_name = models.CharField(max_length=150)
    def __str__(self): return self.vaccine_name

class VaccineRecords(models.Model):
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccines, on_delete=models.CASCADE)
    date_administered = models.DateField()
    dose = models.CharField(max_length=50)

class MortalityRecords(models.Model):
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    date = models.DateField()
    count = models.IntegerField()
    cause = models.CharField(max_length=255)

class EggCollection(models.Model):
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    date = models.DateField()
    eggs_collected = models.IntegerField()
    broken = models.IntegerField(default=0)

class VetVisits(models.Model):
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    visit_date = models.DateField()
    vet_name = models.CharField(max_length=150)
    findings = models.TextField()

class FarmTasks(models.Model):
    
    task = models.CharField(max_length=255)
    # Links to Employee in hr_admin
    assigned_to = models.ForeignKey('hr_admin.EmployeeBasic', on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending','Pending'), ('Done','Done')])