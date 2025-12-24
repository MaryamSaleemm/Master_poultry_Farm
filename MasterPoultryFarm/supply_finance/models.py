from django.db import models

class FeedTypes(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self): return self.name

class FeedSuppliers(models.Model):
    supplier_name = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    def __str__(self): return self.supplier_name

class FeedPurchases(models.Model):
    supplier = models.ForeignKey(FeedSuppliers, on_delete=models.CASCADE)
    feed_type = models.ForeignKey(FeedTypes, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=12, decimal_places=2)

class Customers(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=100)
    def __str__(self): return self.name

class Sales(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

class ExpenseCategories(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self): return self.name

class FarmExpenses(models.Model):
    category = models.ForeignKey(ExpenseCategories, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()