from rest_framework import viewsets
from .models import *
from .serializers import *

class BirdBreedsViewSet(viewsets.ModelViewSet):
    queryset = BirdBreeds.objects.all()
    serializer_class = BirdBreedsSerializer

class BatchesViewSet(viewsets.ModelViewSet):
    queryset = Batches.objects.all()
    serializer_class = BatchesSerializer

class VaccinesViewSet(viewsets.ModelViewSet):
    queryset = Vaccines.objects.all()
    serializer_class = VaccinesSerializer

class VaccineRecordsViewSet(viewsets.ModelViewSet):
    queryset = VaccineRecords.objects.all()
    serializer_class = VaccineRecordsSerializer

class MortalityViewSet(viewsets.ModelViewSet):
    queryset = MortalityRecords.objects.all()
    serializer_class = MortalitySerializer

class EggCollectionViewSet(viewsets.ModelViewSet):
    queryset = EggCollection.objects.all()
    serializer_class = EggCollectionSerializer

class VetVisitsViewSet(viewsets.ModelViewSet):
    queryset = VetVisits.objects.all()
    serializer_class = VetVisitsSerializer

class FarmTasksViewSet(viewsets.ModelViewSet):
    queryset = FarmTasks.objects.all()
    serializer_class = FarmTasksSerializer