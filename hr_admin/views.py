import json
import datetime
from datetime import timedelta
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse
from django import forms
from django.db.models import Sum
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator 

# --- IMPORT MODELS ---
from .models import ToDoItem 
from hr_admin.models import ( 
    EmployeeBasic, EmployeeJob, EmployeeContact, EmployeeAccess, OwnerAddress,
    EmployeeAttendance, EmployeeLeave, EmployeePerformance, Promotions, EmployeeHistory,
    EmployeePayroll, EmployeeBank, EmployeeTax, EmployeeInsurance,
    EmployeeTrainingPrograms, EmployeeTrainingRecords, Branches, EmployeeTermination, TaxRegion
)
from farm_infra.models import FarmBasic, Houses, ConstructionProjects
from poultry_ops.models import Batches, EggCollection
from assets.models import BuildingBasic, OwnerBasic
from supply_finance.models import Sales, FarmExpenses

# --- IMPORT FORMS ---
from . import forms as hr_forms 
from .forms import ToDoItemForm 


#  CONFIGURATION MAPS

MODEL_MAP = {
    'basic': EmployeeBasic, 'contact': EmployeeContact, 'access': EmployeeAccess, 'job': EmployeeJob,
    'promotion': Promotions, 'history': EmployeeHistory, 'termination': EmployeeTermination,
    'payroll': EmployeePayroll, 'bank': EmployeeBank, 'tax': EmployeeTax, 'insurance': EmployeeInsurance,
    'attendance': EmployeeAttendance, 'performance': EmployeePerformance, 'leave': EmployeeLeave,
    'training-programs': EmployeeTrainingPrograms, 'training-records': EmployeeTrainingRecords,
    'address': OwnerAddress, 'branches': Branches, 'taxregion': TaxRegion,
    'todo': ToDoItem, 
}

FORM_MAPPING = {
    'basic': hr_forms.EmployeeBasicForm, 'contact': hr_forms.EmployeeContactForm, 'access': hr_forms.EmployeeAccessForm,
    'job': hr_forms.EmployeeJobForm, 'promotion': hr_forms.PromotionsForm, 'history': hr_forms.EmployeeHistoryForm,
    'termination': hr_forms.EmployeeTerminationForm, 'payroll': hr_forms.EmployeePayrollForm, 'bank': hr_forms.EmployeeBankForm,
    'tax': hr_forms.EmployeeTaxForm, 'insurance': hr_forms.EmployeeInsuranceForm, 'attendance': hr_forms.EmployeeAttendanceForm,
    'performance': hr_forms.EmployeePerformanceForm, 'leave': hr_forms.EmployeeLeaveForm,
    'training-programs': hr_forms.EmployeeTrainingProgramsForm, 'training-records': hr_forms.EmployeeTrainingRecordsForm,
    'address': hr_forms.OwnerAddressForm, 'branches': hr_forms.BranchesForm,
    'todo': hr_forms.ToDoItemForm, 
}

def get_model_by_name(name):
    return MODEL_MAP.get(name)

#  DASHBOARD VIEW

@method_decorator(login_required(login_url='login'), name='dispatch')
class HRDashboardView(TemplateView):
    template_name = 'hr_admin/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Financial Stats
        total_sales = Sales.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        total_expenses = FarmExpenses.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        context['total_sales'] = total_sales
        context['total_expenses'] = total_expenses
        context['net_profit'] = total_sales - total_expenses

        # CHART 1: MONTHLY TRENDS
        six_months_ago = timezone.now() - timedelta(days=180)

        sales_qs = Sales.objects.filter(date__gte=six_months_ago)\
            .annotate(month=TruncMonth('date'))\
            .values('month')\
            .annotate(total=Sum('amount'))\
            .order_by('month')

        expenses_qs = FarmExpenses.objects.filter(date__gte=six_months_ago)\
            .annotate(month=TruncMonth('date'))\
            .values('month')\
            .annotate(total=Sum('amount'))\
            .order_by('month')

        all_months = sorted(list(set([x['month'] for x in sales_qs] + [x['month'] for x in expenses_qs])))
        
        chart_labels = [m.strftime('%b %Y') for m in all_months]
        sales_data = []
        expense_data = []

        for m in all_months:
            s_val = next((item['total'] for item in sales_qs if item['month'] == m), 0)
            e_val = next((item['total'] for item in expenses_qs if item['month'] == m), 0)
            sales_data.append(float(s_val))
            expense_data.append(float(e_val))

        context['chart_labels'] = json.dumps(chart_labels)
        context['sales_data'] = json.dumps(sales_data)
        context['expense_data'] = json.dumps(expense_data)

        # CHART 2: OPERATIONAL COSTS BREAKDOWN
        expense_breakdown = FarmExpenses.objects.values('category__name')\
            .annotate(total=Sum('amount'))\
            .order_by('-total')[:5]

        breakdown_labels = []
        breakdown_data = []
        
        for item in expense_breakdown:

            label = item['category__name'] if item['category__name'] else 'Uncategorized'
            breakdown_labels.append(label)
            breakdown_data.append(float(item['total']))

        context['breakdown_labels'] = json.dumps(breakdown_labels)
        context['breakdown_data'] = json.dumps(breakdown_data)

        # Metrics
        context['total_employees'] = EmployeeBasic.objects.count()
        context['active_batches'] = Batches.objects.count()
        context['total_eggs'] = EggCollection.objects.aggregate(Sum('eggs_collected'))['eggs_collected__sum'] or 0
        context['total_houses'] = Houses.objects.count()
        context['total_farms'] = FarmBasic.objects.count()
        context['total_buildings'] = BuildingBasic.objects.count()
        context['total_owners'] = OwnerBasic.objects.count()
        context['active_projects'] = ConstructionProjects.objects.count()
        
        #  Paginated To-Do List
        todo_queryset = ToDoItem.objects.all().order_by('-created_at')
        paginator = Paginator(todo_queryset, 6)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context['todo_list'] = page_obj
        return context


#  TO-DO LIST
@login_required(login_url='login')
def todo_list_page(request):
    todos = ToDoItem.objects.all().order_by('-created_at')
    context = {
        'todo_list': todos,
        'page_title': 'To Do List Management'
    }
    return render(request, 'hr_admin/todo_list_page.html', context)

#  API VIEWS
@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_todo = ToDoItem.objects.create(title=data['title'])
            return JsonResponse({'status': 'success', 'id': new_todo.id, 'title': new_todo.title})
        except Exception as e: return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def delete_todo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            todo = ToDoItem.objects.get(id=data.get('id'))
            todo.delete()
            return JsonResponse({'status': 'success'})
        except: return JsonResponse({'status': 'error'}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def toggle_todo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            todo = ToDoItem.objects.get(id=data.get('id'))
            todo.is_done = not todo.is_done
            todo.save()
            return JsonResponse({'status': 'success'})
        except: return JsonResponse({'status': 'error'}, status=400)
    return JsonResponse({'status': 'error'}, status=400)


#  UNIVERSAL VIEWS
class UniversalListView(ListView):
    template_name = 'hr_admin/universal_list.html' 
    paginate_by = 8

    def get_queryset(self):
        self.model_class = get_model_by_name(self.kwargs['model_name'])
        return self.model_class.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not hasattr(self, 'model_class'): self.model_class = get_model_by_name(self.kwargs['model_name'])
        
        all_fields = list(self.model_class._meta.fields)
        raw_fields = all_fields[:6]
        
        context['headers'] = [f.verbose_name.title() if f.name != 'id' else 'ID' for f in raw_fields]
        
        rows = []
        for obj in context['object_list']:
            row_data = {'pk': obj.pk, 'values': []}
            for field in raw_fields:
                value = getattr(obj, field.name)
                
                if isinstance(value, (datetime.datetime)):
                    value = value.strftime("%b %d, %Y %I:%M %p")
                elif isinstance(value, (datetime.date)):
                    value = value.strftime("%b %d, %Y")

                if hasattr(obj, f'get_{field.name}_display'):
                    value = getattr(obj, f'get_{field.name}_display')()
                if value is None: value = "-"
                row_data['values'].append(str(value))
            rows.append(row_data)

        context['data_rows'] = rows
        context['model_name'] = self.kwargs['model_name'] 
        context['verbose_name'] = self.model_class._meta.verbose_name_plural.title()

        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
            context['add_url'] = reverse('universal_create', kwargs={'model_name': self.kwargs['model_name']})
            context['update_url_name'] = 'universal_edit'
            context['delete_url_name'] = 'universal_delete'
        else:
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
        return FORM_MAPPING.get(self.kwargs['model_name'].lower()) or forms.modelform_factory(self.model_class, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name']
        context['action'] = "Create"
        try:
            view_name = self.request.resolver_match.url_name.replace('_create', '_list')
            if 'universal' in view_name:
                context['back_url'] = reverse(view_name, kwargs={'model_name': self.kwargs['model_name']})
            else:
                context['back_url'] = reverse(view_name)
        except:
            context['back_url'] = reverse('hr_dashboard')
        return context

    def get_success_url(self):
        view_name = self.request.resolver_match.url_name.replace('_create', '_list')
        if 'universal' in view_name:
             return reverse(view_name, kwargs={'model_name': self.kwargs['model_name']})
        return reverse(view_name)

class UniversalUpdateView(UpdateView):
    template_name = 'hr_admin/universal_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.model_class = get_model_by_name(self.kwargs['model_name'])
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_form_class(self):
        return FORM_MAPPING.get(self.kwargs['model_name'].lower()) or forms.modelform_factory(self.model_class, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name']
        context['action'] = "Edit"
        try:
            view_name = self.request.resolver_match.url_name.replace('_update', '_list')
            if 'universal' in view_name:
                context['back_url'] = reverse(view_name, kwargs={'model_name': self.kwargs['model_name']})
            else:
                context['back_url'] = reverse(view_name)
        except:
            context['back_url'] = reverse('hr_dashboard')
        return context

    def get_success_url(self):
        view_name = self.request.resolver_match.url_name.replace('_update', '_list')
        if 'universal' in view_name:
             return reverse(view_name, kwargs={'model_name': self.kwargs['model_name']})
        return reverse(view_name)

class UniversalDeleteView(DeleteView):
    template_name = 'hr_admin/universal_confirm_delete.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.model_class = get_model_by_name(self.kwargs['model_name'])
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            view_name = self.request.resolver_match.url_name.replace('_delete', '_list')
            if 'universal' in view_name:
                context['back_url'] = reverse(view_name, kwargs={'model_name': self.kwargs['model_name']})
            else:
                context['back_url'] = reverse(view_name)
        except:
            context['back_url'] = reverse('hr_dashboard')
        return context

    def get_success_url(self):
        view_name = self.request.resolver_match.url_name.replace('_delete', '_list')
        if 'universal' in view_name:
             return reverse(view_name, kwargs={'model_name': self.kwargs['model_name']})
        return reverse(view_name)