from django import forms
from .models import (
    OwnerBasic, OwnerContact, OwnerAddress,
    BuildingBasic, BuildingLocation, BuildingSpecs, BuildingFacilities, BuildingManagement,
    Permits, Licenses, BuildingInspections
)
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class OwnerBasicForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = OwnerBasic
        fields = '__all__'

class OwnerContactForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = OwnerContact
        fields = '__all__'

class OwnerAddressForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = OwnerAddress
        fields = '__all__'

class BuildingBasicForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = BuildingBasic
        fields = '__all__'

class BuildingLocationForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = BuildingLocation
        fields = '__all__'
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'step': 'any'}),
        }

class BuildingSpecsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = BuildingSpecs
        fields = '__all__'

class BuildingFacilitiesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = BuildingFacilities
        fields = '__all__'
        widgets = {
            'additional_notes': forms.Textarea(attrs={'rows': 3}),
        }

class BuildingManagementForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = BuildingManagement
        fields = '__all__'

class PermitsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Permits
        fields = '__all__'
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

class LicensesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Licenses
        fields = '__all__'
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

class BuildingInspectionsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = BuildingInspections
        fields = '__all__'
        widgets = {
            'inspection_date': forms.DateInput(attrs={'type': 'date'}),
            'report': forms.Textarea(attrs={'rows': 5}),
        }