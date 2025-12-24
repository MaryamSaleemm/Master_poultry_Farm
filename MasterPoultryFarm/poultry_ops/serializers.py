from rest_framework import serializers
from .models import *

class BirdBreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdBreeds
        fields = '__all__'

class BatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = '__all__'

class VaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccines
        fields = '__all__'

class VaccineRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineRecords
        fields = '__all__'

class MortalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MortalityRecords
        fields = '__all__'

class EggCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EggCollection
        fields = '__all__'

class VetVisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetVisits
        fields = '__all__'

class FarmTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmTasks
        fields = '__all__'