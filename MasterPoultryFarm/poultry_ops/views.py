from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django import forms
from .models import * # Keep this, as it is needed for the forms
from .utils import get_model_by_name

# --- UNIVERSAL ENGINE (For HTML/Web Admin) ---

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

        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
            context['add_url'] = reverse('universal_create', kwargs={'model_name': self.kwargs['model_name']})
            context['update_url_name'] = 'universal_edit'
            context['delete_url_name'] = 'universal_delete'
        else:
            target_create = current_url.replace('_list', '_create')
            context['add_url'] = reverse(target_create)
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
        
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
            context['back_url'] = reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        else:
            target_list = current_url.replace('_create', '_list')
            context['back_url'] = reverse(target_list)
        return context

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
             return reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        return reverse(current_url.replace('_create', '_list'))

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
        
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
            context['back_url'] = reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        else:
            target_list = current_url.replace('_update', '_list')
            context['back_url'] = reverse(target_list)
        return context

    def get_success_url(self):
        current_url = self.request.resolver_match.url_name
        if 'universal' in current_url:
             return reverse('universal_list', kwargs={'model_name': self.kwargs['model_name']})
        return reverse(current_url.replace('_update', '_list'))

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
        return reverse(current_url.replace('_delete', '_list'))