from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django import forms

from .models import (
    FeedTypes, FeedSuppliers, FeedPurchases,
    Customers, Sales, ExpenseCategories, FarmExpenses
)
from . import forms as app_forms

MODEL_MAP = {
    'feed_types': FeedTypes,
    'feed_suppliers': FeedSuppliers,
    'feed_purchases': FeedPurchases,
    'customers': Customers,
    'sales': Sales,
    'expense_categories': ExpenseCategories,
    'farm_expenses': FarmExpenses,
}

def get_model_by_name(name):
    return MODEL_MAP.get(name)

FORM_MAPPING = {
    'feed_types': app_forms.FeedTypesForm,
    'feed_suppliers': app_forms.FeedSuppliersForm,
    'feed_purchases': app_forms.FeedPurchasesForm,
    'customers': app_forms.CustomersForm,
    'sales': app_forms.SalesForm,
    'expense_categories': app_forms.ExpenseCategoriesForm,
    'farm_expenses': app_forms.FarmExpensesForm,
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
        self.model_class = get_model_by_name(self.kwargs['model_name'])
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