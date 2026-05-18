from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django import forms
from django.db.models import Sum
from .models import FarmStatus 
from django.contrib import messages   

from .models import (
    BirdBreeds, Batches, Vaccines, VaccineRecords,
    MortalityRecords, EggCollection, VetVisits, FarmTasks
)

from . import forms as app_forms

MODEL_MAP = {
    'breeds': BirdBreeds,
    'batches': Batches,
    'mortality': MortalityRecords,
    'vaccines': Vaccines,
    'vaccine-records': VaccineRecords, 
    'vet': VetVisits,
    'eggs': EggCollection,
    'tasks': FarmTasks,
    'farmstatus':FarmStatus,
}

def get_model_by_name(name):
    return MODEL_MAP.get(name)

FORM_MAPPING = {
    'breeds': app_forms.BirdBreedsForm,
    'batches': app_forms.BatchesForm,
    'mortality': app_forms.MortalityRecordsForm,
    'vaccines': app_forms.VaccinesForm,
    'vaccine-records': app_forms.VaccineRecordsForm,
    'vet': app_forms.VetVisitsForm,
    'eggs': app_forms.EggCollectionForm,
    'tasks': app_forms.FarmTasksForm,
    '':app_forms.FarmStatusForm
}

class UniversalListView(ListView):
    template_name = 'hr_admin/universal_list.html'
    paginate_by = 8

    def get_queryset(self):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        return self.model_class.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        raw_fields = [f for f in self.model_class._meta.fields if f.name != 'id'][:5]
        context['headers'] = [f.verbose_name.title() for f in raw_fields]

        rows = []
        for obj in context['object_list']:
            row_data = {
                'pk': obj.pk,
                'values': []
            }
            for field in raw_fields:
                value = getattr(obj, field.name)
                
                if hasattr(obj, f'get_{field.name}_display'):
                    value = getattr(obj, f'get_{field.name}_display')()
                
                if value is None:
                    value = "-"
                
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
                context['update_url_name'] = current_url.replace('_list', '_update')
                context['delete_url_name'] = current_url.replace('_list', '_delete')
            except:
                context['add_url'] = "#"
        
        return context

class UniversalCreateView(CreateView):
    template_name = 'hr_admin/universal_form.html'

    def dispatch(self, request, *args, **kwargs):
        model_name = self.kwargs.get('model_name')
        
        if model_name == 'farmstatus':
            if FarmStatus.objects.exists():
                messages.warning(request, "You can only have one Price Setting. Please edit the existing one.")
                return redirect('poultry_farmstatus_list')
        
        return super().dispatch(request, *args, **kwargs)

    def get_form_class(self):
        raw_name = self.kwargs['model_name']
        lookup_key = raw_name.lower()
        if lookup_key in FORM_MAPPING:
            return FORM_MAPPING[lookup_key]
        return forms.modelform_factory(self.model_class, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name']
        context['action'] = "Create"
        
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
            context['back_url'] = reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        elif '_create' in current_url:
            target_list = current_url.replace('_create', '_list')
            context['back_url'] = reverse(target_list)
        else:
            context['back_url'] = "#"
        return context

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
             return reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        if '_create' in current_url:
            return reverse(current_url.replace('_create', '_list'))
        return "/"

class UniversalUpdateView(UpdateView):
    template_name = 'hr_admin/universal_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.model_class = get_model_by_name(self.kwargs['model_name'])
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_form_class(self):
        raw_name = self.kwargs['model_name']
        lookup_key = raw_name.lower()
        if lookup_key in FORM_MAPPING:
            return FORM_MAPPING[lookup_key]
        return forms.modelform_factory(self.model_class, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name']
        context['action'] = "Edit"
        
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
            context['back_url'] = reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        elif '_update' in current_url:
            target_list = current_url.replace('_update', '_list')
            context['back_url'] = reverse(target_list)
        else:
             context['back_url'] = "#"
        return context

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
             return reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        if '_update' in current_url:
            return reverse(current_url.replace('_update', '_list'))
        return "/"

class UniversalDeleteView(DeleteView):
    template_name = 'hr_admin/universal_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        self.model_class = get_model_by_name(self.kwargs['model_name'])
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
             return reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        if '_delete' in current_url:
            return reverse(current_url.replace('_delete', '_list'))
        return "/"

def public_homepage(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def facilities_page(request):
    return render(request, 'facilities.html')

def products_page(request):
    # 1. Get the latest price data
    status = FarmStatus.objects.first()
    
    # 2. If no data exists yet, create a fake one to prevent errors
    if not status:
        status = FarmStatus(current_tray_price=0, box_price=0, single_egg_price=0)
    return render(request, 'products.html', {'status': status})


def contact_page(request):
    return render(request, 'contact.html')