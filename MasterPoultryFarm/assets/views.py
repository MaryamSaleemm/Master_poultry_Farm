from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django import forms
from .utils import get_model_by_name # Import the necessary utility

# --- UNIVERSAL ENGINE (Standardized for Assets App) ---

class UniversalListView(ListView):
    template_name = 'hr_admin/universal_list.html' 
    paginate_by = 20

    def get_queryset(self):
        # Handle model_name coming from **kwargs (urls.py with dictionary argument)
        model_name = self.kwargs['model_name'] 
        self.model_class = get_model_by_name(model_name)
        
        if self.model_class:
            return self.model_class.objects.all().order_by('-id')
        
        # Fallback for empty queryset if model is not found
        # Requires self.model to be set for the parent class, so we use a safe method
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
            context['fields'] = [f.name for f in self.model_class._meta.fields if f.name != 'id'][:4]
        else:
            context['verbose_name'] = "Unknown Model"
            context['fields'] = []

        # SMART URL LOGIC: Uses the precise names defined in assets/urls.py
        current_url = self.request.resolver_match.url_name
        
        # Example: 'assets_owners_list' -> base_name is 'assets_owners_'
        # We must handle the case where the URL name does not contain '_list' (e.g., assets_universal_list)
        try:
            base_name = current_url.rsplit('_', 1)[0] + '_'
        except:
            # Fallback for the catch-all 'assets_universal_list' 
            # Note: This fallback requires reverse('assets_universal_create', kwargs={'model_name': model_name})
            # Since your specific URLs are non-universal, we assume the structured naming is used for CRUD.
            base_name = 'assets_' # This may fail for specific URLs, but works for the logic below.
        
        context['add_url'] = reverse(base_name + 'create', kwargs={'model_name': model_name})
        context['update_url_name'] = base_name + 'update' # Used with pk in template
        context['delete_url_name'] = base_name + 'delete' # Used with pk in template
            
        return context

class UniversalCreateView(CreateView):
    template_name = 'hr_admin/universal_form.html'

    def dispatch(self, request, *args, **kwargs):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        if not self.model_class:
             raise Exception(f"Model '{model_name}' not found in utils.MODEL_MAP")
        # Assign model to self.model so CreateView can function properly
        self.model = self.model_class
        return super().dispatch(request, *args, **kwargs)

    def get_form_class(self):
        return forms.modelform_factory(self.model_class, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name']
        context['action'] = "Create"
        
        current_url = self.request.resolver_match.url_name
        base_name = current_url.rsplit('_', 1)[0] + '_'
        
        context['back_url'] = reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})
        return context

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        base_name = current_url.rsplit('_', 1)[0] + '_'
        return reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})

class UniversalUpdateView(UpdateView):
    template_name = 'hr_admin/universal_form.html'

    def dispatch(self, request, *args, **kwargs):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        if not self.model_class:
             raise Exception(f"Model '{model_name}' not found in utils.MODEL_MAP")
        self.model = self.model_class
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        # We assume the model_class is correctly set in dispatch
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_form_class(self):
        return forms.modelform_factory(self.model_class, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name']
        context['action'] = "Edit"
        
        current_url = self.request.resolver_match.url_name
        base_name = current_url.rsplit('_', 1)[0] + '_'
        
        context['back_url'] = reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})
        return context

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        base_name = current_url.rsplit('_', 1)[0] + '_'
        return reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})

class UniversalDeleteView(DeleteView):
    template_name = 'hr_admin/universal_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        model_name = self.kwargs['model_name']
        self.model_class = get_model_by_name(model_name)
        if not self.model_class:
             raise Exception(f"Model '{model_name}' not found in utils.MODEL_MAP")
        self.model = self.model_class
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs['pk'])

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        base_name = current_url.rsplit('_', 1)[0] + '_'
        return reverse(base_name + 'list', kwargs={'model_name': self.kwargs['model_name']})