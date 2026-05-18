from django import forms
from .models import (
    FarmBasic, FarmLocation, FarmOwnership, Houses,
    HouseSpecs, HouseUtilities, ConstructionProjects, FarmAudits
)

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class FarmBasicForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FarmBasic
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class FarmLocationForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FarmLocation
        fields = '__all__'

class FarmOwnershipForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FarmOwnership
        fields = '__all__'

class HousesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Houses
        fields = '__all__'

class HouseSpecsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = HouseSpecs
        fields = '__all__'

class HouseUtilitiesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = HouseUtilities
        fields = '__all__'

class ConstructionProjectsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ConstructionProjects
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class FarmAuditsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FarmAudits
        fields = '__all__'
        widgets = {
            'audit_date': forms.DateInput(attrs={'type': 'date'}),
            'report': forms.Textarea(attrs={'rows': 4}),
        }