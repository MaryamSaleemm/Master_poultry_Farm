from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django import forms

# Import Models
from .models import (
    OwnerBasic, OwnerContact, OwnerAddress,
    BuildingBasic, BuildingLocation, BuildingSpecs, BuildingFacilities, BuildingManagement,
    Permits, Licenses, BuildingInspections
)

# Import Forms
from . import forms as app_forms

# Maps and Utils

MODEL_MAP = {
    'owners': OwnerBasic,
    'owner-contacts': OwnerContact,
    'owner-address': OwnerAddress,
    'buildings': BuildingBasic,
    'locations': BuildingLocation,
    'specs': BuildingSpecs,
    'facilities': BuildingFacilities,
    'management': BuildingManagement,
    'permits': Permits,
    'licenses': Licenses,
    'inspections': BuildingInspections,
}

def get_model_by_name(name):
    return MODEL_MAP.get(name)

FORM_MAPPING = {
    'owners': app_forms.OwnerBasicForm,
    'owner-contacts': app_forms.OwnerContactForm,
    'owner-address': app_forms.OwnerAddressForm,
    'buildings': app_forms.BuildingBasicForm,
    'locations': app_forms.BuildingLocationForm,
    'specs': app_forms.BuildingSpecsForm,
    'facilities': app_forms.BuildingFacilitiesForm,
    'management': app_forms.BuildingManagementForm,
    'permits': app_forms.PermitsForm,
    'licenses': app_forms.LicensesForm,
    'inspections': app_forms.BuildingInspectionsForm,
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
            base_name = 'assets_' 
        
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