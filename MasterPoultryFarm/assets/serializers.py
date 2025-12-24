from rest_framework import serializers
from .models import (
    OwnerBasic, OwnerContact, OwnerAddress,
    BuildingBasic, BuildingLocation, BuildingSpecs, BuildingFacilities, BuildingManagement,
    Permits, Licenses, BuildingInspections
)

# --- OWNER SERIALIZERS ---
class OwnerBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerBasic
        fields = '__all__'

class OwnerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerContact
        fields = '__all__'

class OwnerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerAddress
        fields = '__all__'

# --- BUILDING SERIALIZERS ---
class BuildingBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingBasic
        fields = '__all__'

class BuildingLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingLocation
        fields = '__all__'

class BuildingSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingSpecs
        fields = '__all__'

class BuildingFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingFacilities
        fields = '__all__'
        
class BuildingManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingManagement
        fields = '__all__'

# --- COMPLIANCE SERIALIZERS ---
class PermitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permits
        fields = '__all__'

class LicensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenses
        fields = '__all__'

class BuildingInspectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingInspections
        fields = '__all__'