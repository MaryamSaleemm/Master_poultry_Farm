from rest_framework import serializers
from .models import EmployeeBasic, EmployeeJob

# This converts the Employee Database Row -> JSON Text
class EmployeeBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBasic
        fields = '__all__'

# This converts the Job Database Row -> JSON Text
class EmployeeJobSerializer(serializers.ModelSerializer):
    # We can even show the employee's name instead of just their ID
    employee_name = serializers.CharField(source='employee.name', read_only=True)

    class Meta:
        model = EmployeeJob
        fields = '__all__'