from rest_framework import serializers
from .models import (
    FarmBasic, FarmLocation, FarmOwnership, Houses, 
    HouseSpecs, HouseUtilities, ConstructionProjects, FarmAudits
)

class FarmBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmBasic
        fields = '__all__'

class FarmLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmLocation
        fields = '__all__'

class FarmOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmOwnership
        fields = '__all__'

class HousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = '__all__'

class HouseSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseSpecs
        fields = '__all__'

class HouseUtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseUtilities
        fields = '__all__'

class ConstructionProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionProjects
        fields = '__all__'

class FarmAuditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmAudits
        fields = '__all__'