from django import forms
from django.utils import timezone
from .models import (
    OwnerAddress, Branches, EmployeeBasic, EmployeeContact, EmployeeAccess,
    EmployeeJob, Promotions, EmployeeHistory, EmployeeTermination,
    EmployeePayroll, EmployeeBank, EmployeeTax, EmployeeInsurance,
    EmployeeAttendance, EmployeePerformance, EmployeeLeave,
    EmployeeTrainingPrograms, EmployeeTrainingRecords,ToDoItem
)

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class OwnerAddressForm(BootstrapFormMixin, forms.ModelForm):
    class Meta: model = OwnerAddress; fields = '__all__'

class BranchesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta: model = Branches; fields = '__all__'

class EmployeeBasicForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeBasic
        fields = '__all__'
        widgets = {'dob': forms.DateInput(attrs={'type': 'date'})}

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob and dob > timezone.now().date():
            raise forms.ValidationError("Date of Birth cannot be in the future.")
        return dob

class EmployeeContactForm(BootstrapFormMixin, forms.ModelForm):
    class Meta: model = EmployeeContact; fields = '__all__'

class EmployeeAccessForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeAccess
        fields = '__all__'
        widgets = {'rfid_card_number': forms.TextInput(attrs={'placeholder': 'Scan Card Here'})}

class EmployeeJobForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeJob
        fields = '__all__'
        widgets = {'hire_date': forms.DateInput(attrs={'type': 'date'})}

    def clean_hire_date(self):
        hire_date = self.cleaned_data.get('hire_date')
        if hire_date and hire_date > timezone.now().date():
            raise forms.ValidationError("Hire Date cannot be in the future.")
        return hire_date

class PromotionsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Promotions
        fields = '__all__'
        widgets = {'promotion_date': forms.DateInput(attrs={'type': 'date'}), 'notes': forms.Textarea(attrs={'rows': 3})}

class EmployeeHistoryForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeHistory
        fields = '__all__'
        widgets = {'change_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}), 'old_value': forms.Textarea(attrs={'rows': 2}), 'new_value': forms.Textarea(attrs={'rows': 2})}

class EmployeeTerminationForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeTermination
        fields = '__all__'
        widgets = {'termination_date': forms.DateInput(attrs={'type': 'date'}), 'reason': forms.Textarea(attrs={'rows': 3}), 'exit_interview_notes': forms.Textarea(attrs={'rows': 3})}

class EmployeePayrollForm(BootstrapFormMixin, forms.ModelForm):
    class Meta: model = EmployeePayroll; fields = '__all__'

class EmployeeBankForm(BootstrapFormMixin, forms.ModelForm):
    class Meta: model = EmployeeBank; fields = '__all__'

class EmployeeTaxForm(BootstrapFormMixin, forms.ModelForm):
    class Meta: model = EmployeeTax; fields = '__all__'

class EmployeeInsuranceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeInsurance
        fields = '__all__'
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'}), 'end_date': forms.DateInput(attrs={'type': 'date'}), 'coverage_details': forms.Textarea(attrs={'rows': 3})}
    
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")
        if start and end and end < start:
            self.add_error('end_date', "Insurance End Date must be after Start Date.")
        return cleaned_data

class EmployeeAttendanceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeAttendance
        fields = '__all__'
        widgets = {'attendance_date': forms.DateInput(attrs={'type': 'date'}), 'check_in': forms.TimeInput(attrs={'type': 'time'}), 'check_out': forms.TimeInput(attrs={'type': 'time'})}

class EmployeePerformanceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeePerformance
        fields = '__all__'
        widgets = {'review_date': forms.DateInput(attrs={'type': 'date'}), 'notes': forms.Textarea(attrs={'rows': 4})}

class EmployeeLeaveForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeLeave
        fields = '__all__'
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'}), 'end_date': forms.DateInput(attrs={'type': 'date'})}

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")
        if start and end and end < start:
            self.add_error('end_date', "Leave End Date cannot be before Start Date.")
        return cleaned_data

class EmployeeTrainingProgramsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta: model = EmployeeTrainingPrograms; fields = '__all__'

class EmployeeTrainingRecordsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeTrainingRecords
        fields = '__all__'
        widgets = {'enroll_date': forms.DateInput(attrs={'type': 'date'}), 'completion_date': forms.DateInput(attrs={'type': 'date'})}
 
       
class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'is_done']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task description'}),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input ml-2'}),
        }
        labels = {
            'title': 'Task Description',
            'is_done': 'Mark as Completed',
        }      
        