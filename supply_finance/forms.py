from django import forms
from .models import (
    FeedTypes, FeedSuppliers, FeedPurchases,
    Customers, Sales, ExpenseCategories, FarmExpenses
)

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class FeedTypesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FeedTypes
        fields = '__all__'

class FeedSuppliersForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FeedSuppliers
        fields = '__all__'

class FeedPurchasesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FeedPurchases
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class CustomersForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'

class SalesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ExpenseCategoriesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ExpenseCategories
        fields = '__all__'

class FarmExpensesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FarmExpenses
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }