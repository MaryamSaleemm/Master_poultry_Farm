from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse
from django import forms
from django.db.models import Sum
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

# --- IMPORT MODELS ---
from hr_admin.models import (
    EmployeeBasic, EmployeeJob, EmployeeContact, EmployeeAccess, OwnerAddress,
    EmployeeAttendance, EmployeeLeave, EmployeePerformance, Promotions, EmployeeHistory,
    EmployeePayroll, EmployeeBank, EmployeeTax, EmployeeInsurance,
    EmployeeTrainingPrograms, EmployeeTrainingRecords, Branches, EmployeeTermination
)

# Import other app models for the dashboard (wrapped in try/except to prevent crashes)
try:
    from farm_infra.models import FarmBasic, Houses, ConstructionProjects
    from poultry_ops.models import Batches, EggCollection
    from assets.models import BuildingBasic, OwnerBasic
    from supply_finance.models import Sales, FarmExpenses
except ImportError:
    pass 

from .utils import get_model_by_name

# ==========================================
# 1. WEB DASHBOARD VIEWS (Restored)
# ==========================================

class HRDashboardView(TemplateView):
    template_name = 'hr_admin/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 1. HR METRICS
        context['total_employees'] = EmployeeBasic.objects.count()
        
        # 2. OTHER METRICS
        try: context['total_farms'] = FarmBasic.objects.count()
        except: context['total_farms'] = 0
            
        try: context['active_batches'] = Batches.objects.count()
        except: context['active_batches'] = 0

        # You can add more metrics here as needed
        return context

# ==========================================
# 2. UNIVERSAL VIEWS (Restored)
# ==========================================

class UniversalListView(ListView):
    template_name = 'hr_admin/universal_list.html' 
    paginate_by = 20

    def get_queryset(self):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        return self.model_class.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name'] 
        context['verbose_name'] = self.model_class._meta.verbose_name_plural.title()
        context['fields'] = [f.name for f in self.model_class._meta.fields if f.name != 'id'][:4]
        
        # URL Logic
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
            context['add_url'] = reverse('universal_create', kwargs={'model_name': self.kwargs['model_name']})
            context['update_url_name'] = 'universal_edit'
            context['delete_url_name'] = 'universal_delete'
        else:
            # Fallback for specific named urls
            try:
                target_create = current_url.replace('_list', '_create')
                context['add_url'] = reverse(target_create)
            except:
                context['add_url'] = "#"
            context['update_url_name'] = current_url.replace('_list', '_update')
            context['delete_url_name'] = current_url.replace('_list', '_delete')
        return context

class UniversalCreateView(CreateView):
    template_name = 'hr_admin/universal_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.model_class = get_model_by_name(self.kwargs['model_name'])
        return super().dispatch(request, *args, **kwargs)

    def get_form_class(self):
        return forms.modelform_factory(self.model_class, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name']
        context['action'] = "Create"
        return context

    def get_success_url(self):
        try:
            return reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        except:
             return reverse('hr_dashboard') # Fallback

class UniversalUpdateView(UpdateView):
    template_name = 'hr_admin/universal_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.model_class = get_model_by_name(self.kwargs['model_name'])
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_form_class(self):
        return forms.modelform_factory(self.model_class, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name']
        context['action'] = "Edit"
        return context

    def get_success_url(self):
        try:
            return reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        except:
             return reverse('hr_dashboard')

class UniversalDeleteView(DeleteView):
    template_name = 'hr_admin/universal_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        self.model_class = get_model_by_name(self.kwargs['model_name'])
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_success_url(self):
        try:
            return reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        except:
             return reverse('hr_dashboard')

# ==========================================
# 3. API SERIALIZERS & VIEWSETS (For Flutter)
# ==========================================

# --- Serializers ---
class EmployeeBasicSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeBasic; fields = '__all__'

class EmployeeJobSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeJob; fields = '__all__'

class EmployeeContactSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeContact; fields = '__all__'

class EmployeeAccessSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeAccess; fields = '__all__'

class OwnerAddressSerializer(serializers.ModelSerializer):
    class Meta: model = OwnerAddress; fields = '__all__'

class EmployeeAttendanceSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeAttendance; fields = '__all__'

class EmployeeLeaveSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeLeave; fields = '__all__'

class EmployeePerformanceSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeePerformance; fields = '__all__'

class PromotionsSerializer(serializers.ModelSerializer):
    class Meta: model = Promotions; fields = '__all__'

class EmployeeHistorySerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeHistory; fields = '__all__'

class EmployeePayrollSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeePayroll; fields = '__all__'

class EmployeeBankSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeBank; fields = '__all__'

class EmployeeTaxSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeTax; fields = '__all__'

class EmployeeInsuranceSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeInsurance; fields = '__all__'
    
class EmployeeTrainingProgramsSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeTrainingPrograms; fields = '__all__'

class EmployeeTrainingRecordsSerializer(serializers.ModelSerializer):
    class Meta: model = EmployeeTrainingRecords; fields = '__all__'

class BranchesSerializer(serializers.ModelSerializer):
    class Meta: model = Branches; fields = '__all__'

# --- ViewSets ---
class EmployeeBasicViewSet(viewsets.ModelViewSet):
    queryset = EmployeeBasic.objects.all()
    serializer_class = EmployeeBasicSerializer

class EmployeeJobViewSet(viewsets.ModelViewSet):
    queryset = EmployeeJob.objects.all()
    serializer_class = EmployeeJobSerializer

class EmployeeContactViewSet(viewsets.ModelViewSet):
    queryset = EmployeeContact.objects.all()
    serializer_class = EmployeeContactSerializer

class EmployeeAccessViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAccess.objects.all()
    serializer_class = EmployeeAccessSerializer

class OwnerAddressViewSet(viewsets.ModelViewSet):
    queryset = OwnerAddress.objects.all()
    serializer_class = OwnerAddressSerializer

class EmployeeAttendanceViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAttendance.objects.all()
    serializer_class = EmployeeAttendanceSerializer

class EmployeeLeaveViewSet(viewsets.ModelViewSet):
    queryset = EmployeeLeave.objects.all()
    serializer_class = EmployeeLeaveSerializer

class EmployeePerformanceViewSet(viewsets.ModelViewSet):
    queryset = EmployeePerformance.objects.all()
    serializer_class = EmployeePerformanceSerializer

class PromotionsViewSet(viewsets.ModelViewSet):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer

class EmployeeHistoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeeHistory.objects.all()
    serializer_class = EmployeeHistorySerializer

class EmployeePayrollViewSet(viewsets.ModelViewSet):
    queryset = EmployeePayroll.objects.all()
    serializer_class = EmployeePayrollSerializer

class EmployeeBankViewSet(viewsets.ModelViewSet):
    queryset = EmployeeBank.objects.all()
    serializer_class = EmployeeBankSerializer

class EmployeeTaxViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTax.objects.all()
    serializer_class = EmployeeTaxSerializer

class EmployeeInsuranceViewSet(viewsets.ModelViewSet):
    queryset = EmployeeInsurance.objects.all()
    serializer_class = EmployeeInsuranceSerializer
    
class EmployeeTrainingProgramsViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTrainingPrograms.objects.all()
    serializer_class = EmployeeTrainingProgramsSerializer

class EmployeeTrainingRecordsViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTrainingRecords.objects.all()
    serializer_class = EmployeeTrainingRecordsSerializer

class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer

# --- Dashboard API Stats ---
class DashboardStatsAPI(APIView):
    def get(self, request):
        stats = {
            "total_employees": EmployeeBasic.objects.count(),
            "total_branches": Branches.objects.count(),
            "active_jobs": EmployeeJob.objects.filter(status='Active').count(),
        }
        return Response(stats)