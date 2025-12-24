from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse
from django import forms
from .models import *
from .utils import get_model_by_name

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
# --- UNIVERSAL ENGINE (Identical Logic) ---

class UniversalListView(ListView):
    # REUSING TEMPLATES FROM HR_ADMIN APP
    template_name = 'hr_admin/universal_list.html' 
    paginate_by = 20

    def get_queryset(self):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        # Added .order_by('-id') to show newest items first and fix the warning
        return self.model_class.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Standard Data
        context['model_name'] = self.kwargs['model_name'] 
        context['verbose_name'] = self.model_class._meta.verbose_name_plural.title()
        context['fields'] = [f.name for f in self.model_class._meta.fields if f.name != 'id'][:4]

        # 2. SMART URL CALCULATION
        # We find out "Where are we now?" (e.g., 'employee_basic_list')
        current_url = self.request.resolver_match.url_name
        
        if 'universal' in current_url:
            # FALLBACK: If we are on the old generic URL, use generic links
            context['add_url'] = reverse('universal_create', kwargs={'model_name': self.kwargs['model_name']})
            context['update_url_name'] = 'universal_edit'
            context['delete_url_name'] = 'universal_delete'
        else:
            # MANUAL MODE: We are on 'employee_basic_list', so we want 'employee_basic_create'
            # We swap '_list' for '_create'
            target_create_name = current_url.replace('_list', '_create')
            
            # We calculate the actual link (e.g., "/employees/add/")
            context['add_url'] = reverse(target_create_name)
            
            # For the table rows (Edit/Delete), we just send the NAME, not the full link
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
        context['action'] = "Edit" if isinstance(self, UpdateView) else "Create"
        
        # --- SMART BACK BUTTON LOGIC ---
        current_url = self.request.resolver_match.url_name
        
        if 'universal' in current_url:
            # Fallback
            context['back_url'] = reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        else:
            # Manual Mode: Swap '_create' or '_update' back to '_list'
            if '_create' in current_url:
                target_list = current_url.replace('_create', '_list')
            elif '_update' in current_url:
                target_list = current_url.replace('_update', '_list')
            else:
                target_list = current_url # Should not happen
                
            context['back_url'] = reverse(target_list)
            
        return context

    # We redirect back to the LIST view of the same model
    def get_success_url(self):
        # 1. Check where we came from
        current_url = self.request.resolver_match.url_name
        
        # 2. If we are on the 'Ugly' generic URL, stay there (Fallback)
        if 'universal' in current_url:
             return reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        
        # 3. If we are on a 'Clean' manual URL, go back to the clean list
        # Example: 'employee_basic_create' -> 'employee_basic_list'
        if '_create' in current_url:
            target_list = current_url.replace('_create', '_list')
        elif '_update' in current_url:
            target_list = current_url.replace('_update', '_list')
        else:
            # Should not happen, but safe fallback
            target_list = current_url 
            
        return reverse(target_list)

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
        context['action'] = "Edit" if isinstance(self, UpdateView) else "Create"
        
        # --- SMART BACK BUTTON LOGIC ---
        current_url = self.request.resolver_match.url_name
        
        if 'universal' in current_url:
            # Fallback
            context['back_url'] = reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        else:
            # Manual Mode: Swap '_create' or '_update' back to '_list'
            if '_create' in current_url:
                target_list = current_url.replace('_create', '_list')
            elif '_update' in current_url:
                target_list = current_url.replace('_update', '_list')
            else:
                target_list = current_url # Should not happen
                
            context['back_url'] = reverse(target_list)
            
        return context

    def get_success_url(self):
        return reverse(f'farm_{self.kwargs["model_name"]}_list')

class UniversalDeleteView(DeleteView):
    template_name = 'hr_admin/universal_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        self.model_class = get_model_by_name(self.kwargs['model_name'])
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse(f'farm_{self.kwargs["model_name"]}_list')