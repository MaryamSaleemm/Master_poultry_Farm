from rest_framework import viewsets
from .models import (
    OwnerBasic, OwnerContact, OwnerAddress,
    BuildingBasic, BuildingLocation, BuildingSpecs, BuildingFacilities, BuildingManagement,
    Permits, Licenses, BuildingInspections
)
from .serializers import (
    OwnerBasicSerializer, OwnerContactSerializer, OwnerAddressSerializer,
    BuildingBasicSerializer, BuildingLocationSerializer, BuildingSpecsSerializer,
    BuildingFacilitiesSerializer, BuildingManagementSerializer,
    PermitsSerializer, LicensesSerializer, BuildingInspectionsSerializer
)

# --- OWNER VIEWSETS ---
class OwnerBasicViewSet(viewsets.ModelViewSet):
    queryset = OwnerBasic.objects.all().order_by('-id')
    serializer_class = OwnerBasicSerializer

class OwnerContactViewSet(viewsets.ModelViewSet):
    queryset = OwnerContact.objects.all().order_by('-id')
    serializer_class = OwnerContactSerializer

class OwnerAddressViewSet(viewsets.ModelViewSet):
    queryset = OwnerAddress.objects.all().order_by('-id')
    serializer_class = OwnerAddressSerializer

# --- BUILDING VIEWSETS ---
class BuildingBasicViewSet(viewsets.ModelViewSet):
    queryset = BuildingBasic.objects.all().order_by('-id')
    serializer_class = BuildingBasicSerializer

class BuildingLocationViewSet(viewsets.ModelViewSet):
    queryset = BuildingLocation.objects.all().order_by('-id')
    serializer_class = BuildingLocationSerializer

class BuildingSpecsViewSet(viewsets.ModelViewSet):
    queryset = BuildingSpecs.objects.all().order_by('-id')
    serializer_class = BuildingSpecsSerializer

class BuildingFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = BuildingFacilities.objects.all().order_by('-id')
    serializer_class = BuildingFacilitiesSerializer
    
class BuildingManagementViewSet(viewsets.ModelViewSet):
    queryset = BuildingManagement.objects.all().order_by('-id')
    serializer_class = BuildingManagementSerializer

# --- COMPLIANCE VIEWSETS ---
class PermitsViewSet(viewsets.ModelViewSet):
    queryset = Permits.objects.all().order_by('-id')
    serializer_class = PermitsSerializer

class LicensesViewSet(viewsets.ModelViewSet):
    queryset = Licenses.objects.all().order_by('-id')
    serializer_class = LicensesSerializer

class BuildingInspectionsViewSet(viewsets.ModelViewSet):
    queryset = BuildingInspections.objects.all().order_by('-id')
    serializer_class = BuildingInspectionsSerializer