from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django import forms

# Import Models
from .models import (
    FarmBasic, FarmLocation, FarmOwnership, Houses,
    HouseSpecs, HouseUtilities, ConstructionProjects, FarmAudits
)

# Import Forms
from . import forms as app_forms

# Maps and Utils

MODEL_MAP = {
    'basic': FarmBasic,
    'location': FarmLocation,
    'ownership': FarmOwnership,
    'houses': Houses,
    'specs': HouseSpecs,
    'utilities': HouseUtilities,
    'construction': ConstructionProjects,
    'audits': FarmAudits,
}

def get_model_by_name(name):
    return MODEL_MAP.get(name)

FORM_MAPPING = {
    'basic': app_forms.FarmBasicForm,
    'location': app_forms.FarmLocationForm,
    'ownership': app_forms.FarmOwnershipForm,
    'houses': app_forms.HousesForm,
    'specs': app_forms.HouseSpecsForm,
    'utilities': app_forms.HouseUtilitiesForm,
    'construction': app_forms.ConstructionProjectsForm,
    'audits': app_forms.FarmAuditsForm,
}

# Universal Engine

class UniversalListView(ListView):
    template_name = 'hr_admin/universal_list.html' 
    paginate_by = 8

    def get_queryset(self):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        if self.model_class:
            return self.model_class.objects.all().order_by('-id')
        try:
            return self.model.objects.none() 
        except AttributeError:
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs['model_name']
        context['model_name'] = model_name
        
        if self.model_class:
            context['verbose_name'] = self.model_class._meta.verbose_name_plural.title()
            
            # Pick first 4 fields to keep table clean
            raw_fields = [f for f in self.model_class._meta.fields if f.name != 'id'][:4]
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
        else:
            context['verbose_name'] = "Unknown Model"
            context['headers'] = []
            context['data_rows'] = []
        
        current_url = self.request.resolver_match.url_name
        try:
            base_name = current_url.rsplit('_', 1)[0] + '_'
        except:
            base_name = 'farm_infra_' 
        
        context['add_url'] = reverse(base_name + 'create', kwargs={'model_name': model_name})
        context['update_url_name'] = base_name + 'update'
        context['delete_url_name'] = base_name + 'delete'
            
        return context

class UniversalCreateView(CreateView):
    template_name = 'hr_admin/universal_form.html'

    def dispatch(self, request, *args, **kwargs):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        if not self.model_class:
             raise Exception(f"Model '{model_name}' not found in MODEL_MAP")
        self.model = self.model_class
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
        try:
            base_name = current_url.rsplit('_', 1)[0] + '_'
            context['back_url'] = reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})
        except:
            context['back_url'] = "#"
        return context

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        try:
            base_name = current_url.rsplit('_', 1)[0] + '_'
            return reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})
        except:
            return "/"

class UniversalUpdateView(UpdateView):
    template_name = 'hr_admin/universal_form.html'

    def dispatch(self, request, *args, **kwargs):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        if not self.model_class:
             raise Exception(f"Model '{model_name}' not found in MODEL_MAP")
        self.model = self.model_class
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
        try:
            base_name = current_url.rsplit('_', 1)[0] + '_'
            context['back_url'] = reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})
        except:
            context['back_url'] = "#"
        return context

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        try:
            base_name = current_url.rsplit('_', 1)[0] + '_'
            return reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})
        except:
            return "/"

class UniversalDeleteView(DeleteView):
    template_name = 'hr_admin/universal_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        if not self.model_class:
             raise Exception(f"Model '{model_name}' not found in MODEL_MAP")
        self.model = self.model_class
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        try:
            base_name = current_url.rsplit('_', 1)[0] + '_'
            return reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})
        except:
            return "/"