from rest_framework import viewsets
from .models import (
    FarmBasic, FarmLocation, FarmOwnership, Houses, 
    HouseSpecs, HouseUtilities, ConstructionProjects, FarmAudits
)
from .serializers import (
    FarmBasicSerializer, FarmLocationSerializer, FarmOwnershipSerializer, 
    HousesSerializer, HouseSpecsSerializer, HouseUtilitiesSerializer, 
    ConstructionProjectsSerializer, FarmAuditsSerializer
)

class FarmBasicViewSet(viewsets.ModelViewSet):
    queryset = FarmBasic.objects.all().order_by('-id')
    serializer_class = FarmBasicSerializer

class FarmLocationViewSet(viewsets.ModelViewSet):
    queryset = FarmLocation.objects.all().order_by('-id')
    serializer_class = FarmLocationSerializer

class FarmOwnershipViewSet(viewsets.ModelViewSet):
    queryset = FarmOwnership.objects.all().order_by('-id')
    serializer_class = FarmOwnershipSerializer

class HousesViewSet(viewsets.ModelViewSet):
    queryset = Houses.objects.all().order_by('-id')
    serializer_class = HousesSerializer

class HouseSpecsViewSet(viewsets.ModelViewSet):
    queryset = HouseSpecs.objects.all().order_by('-id')
    serializer_class = HouseSpecsSerializer

class HouseUtilitiesViewSet(viewsets.ModelViewSet):
    queryset = HouseUtilities.objects.all().order_by('-id')
    serializer_class = HouseUtilitiesSerializer

class ConstructionProjectsViewSet(viewsets.ModelViewSet):
    queryset = ConstructionProjects.objects.all().order_by('-id')
    serializer_class = ConstructionProjectsSerializer

class FarmAuditsViewSet(viewsets.ModelViewSet):
    queryset = FarmAudits.objects.all().order_by('-id')
    serializer_class = FarmAuditsSerializer