from rest_framework import serializers
from .models import *

class SalesSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    class Meta:
        model = Sales
        fields = '__all__'

class ExpensesSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = FarmExpenses
        fields = '__all__'