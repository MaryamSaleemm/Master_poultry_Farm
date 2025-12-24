from rest_framework import viewsets
from .models import *
from .serializers import SalesSerializer, ExpensesSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all().order_by('-id')
    serializer_class = SalesSerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = FarmExpenses.objects.all().order_by('-id')
    serializer_class = ExpensesSerializer