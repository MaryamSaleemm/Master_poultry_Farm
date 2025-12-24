from django.db import models

class FarmBasic(models.Model):
    farm_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    def __str__(self): return self.farm_name

class FarmLocation(models.Model):
    farm = models.ForeignKey(FarmBasic, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

class FarmOwnership(models.Model):
    farm = models.ForeignKey(FarmBasic, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=150)
    owner_contact = models.CharField(max_length=100)

class Houses(models.Model):
    TYPES = [('Layer', 'Layer'), ('Broiler', 'Broiler'), ('Breeder', 'Breeder')]
    farm = models.ForeignKey(FarmBasic, on_delete=models.CASCADE)
    house_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPES)
    def __str__(self): return self.house_name

class HouseSpecs(models.Model):
    house = models.ForeignKey(Houses, on_delete=models.CASCADE)
    floor_area = models.DecimalField(max_digits=10, decimal_places=2)
    ventilation_type = models.CharField(max_length=100)

class HouseUtilities(models.Model):
    house = models.ForeignKey(Houses, on_delete=models.CASCADE)
    electricity = models.BooleanField(default=True)
    water_source = models.CharField(max_length=100)

class ConstructionProjects(models.Model):
    farm = models.ForeignKey(FarmBasic, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()

class FarmAudits(models.Model):
    farm = models.ForeignKey(FarmBasic, on_delete=models.CASCADE)
    audit_date = models.DateField()
    auditor_name = models.CharField(max_length=150)
    report = models.TextField()