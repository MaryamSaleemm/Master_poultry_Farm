from django.db import models
from django.core.exceptions import ValidationError


def validate_phone(value):
    import re
    pattern = re.compile(r'^(\+92|0)?3\d{9}$')
    if not pattern.match(value):
        raise ValidationError('Enter a valid phone number (e.g., 03001234567).')

def validate_positive(value):
    if value < 0:
        raise ValidationError('This value cannot be negative.')

def validate_non_zero(value):
    if value <= 0:
        raise ValidationError('This value must be greater than zero.')

# Feed and Suppliers

class FeedTypes(models.Model):
    name = models.CharField(max_length=150, unique=True)
    
    class Meta:
        verbose_name = "Feed Types"
        verbose_name_plural = "Feed Types"
    def __str__(self): return self.name

class FeedSuppliers(models.Model):
    supplier_name = models.CharField(max_length=150, unique=True)
    contact = models.CharField(
        max_length=15, 
        validators=[validate_phone], 
        help_text="Format: 03001234567"
    )
    class Meta:
        verbose_name = "Feed Suppliers"
        verbose_name_plural = "Feed Suppliers"

    def clean(self):
        if FeedSuppliers.objects.filter(supplier_name__iexact=self.supplier_name).exclude(pk=self.pk).exists():
            raise ValidationError({'supplier_name': f"Supplier '{self.supplier_name}' already exists."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(FeedSuppliers, self).save(*args, **kwargs)

    def __str__(self): return self.supplier_name

class FeedPurchases(models.Model):
    supplier = models.ForeignKey(FeedSuppliers, on_delete=models.CASCADE)
    feed_type = models.ForeignKey(FeedTypes, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_non_zero], help_text="In kg/bags")
    cost = models.DecimalField(max_digits=12, decimal_places=2, validators=[validate_positive])
    class Meta:
        verbose_name = "Feed Purchases"
        verbose_name_plural = "Feed Purchases"
    def __str__(self):
        return f"{self.feed_type} - {self.date}"

# Customers and Sales

class Customers(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(
        max_length=15, 
        validators=[validate_phone], 
        unique=True,
        help_text="Format: 03001234567"
    )
    class Meta:
        verbose_name = "Customers"
        verbose_name_plural = "Customers"

    def __str__(self): return self.name

class Sales(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[validate_positive])

    class Meta:
        verbose_name = "Sales"
        verbose_name_plural = "Sales"
    def __str__(self):
        return f"{self.product} - {self.amount}"

# Expenses

class ExpenseCategories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    def __str__(self): return self.name

class FarmExpenses(models.Model):
    category = models.ForeignKey(ExpenseCategories, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[validate_positive])
    description = models.TextField()

    class Meta:
        verbose_name = "Expenses Categories"
        verbose_name_plural = "Expenses Categories"
    def __str__(self):
        return f"{self.category} - {self.amount}"