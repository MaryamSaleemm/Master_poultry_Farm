from django import forms
from .models import (
    BirdBreeds, Batches, Vaccines, VaccineRecords,
    MortalityRecords, EggCollection, VetVisits, FarmTasks,FarmStatus
)

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class BirdBreedsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = BirdBreeds
        fields = '__all__'

class BatchesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Batches
        fields = '__all__'
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
        }

class VaccinesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Vaccines
        fields = '__all__'

class VaccineRecordsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = VaccineRecords
        fields = '__all__'
        widgets = {
            'date_administered': forms.DateInput(attrs={'type': 'date'}),
        }

class MortalityRecordsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = MortalityRecords
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class EggCollectionForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EggCollection
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class VetVisitsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = VetVisits
        fields = '__all__'
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
            'findings': forms.Textarea(attrs={'rows': 4}),
        }

class FarmTasksForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FarmTasks
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
class FarmStatusForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FarmStatus
        fields = ['single_egg_price', 'current_tray_price', 'box_price', 'eggs_in_stock', 'hens_in_stock']
        labels = {
            'single_egg_price': 'Single Egg Price (Rs)',
            'current_tray_price': 'Tray Price (30 Eggs)',
            'box_price': 'Box Price (360 Eggs)',
            'eggs_in_stock': 'Are Eggs In Stock?',
            'hens_in_stock': 'Are Cull Birds Available?',
        }
        