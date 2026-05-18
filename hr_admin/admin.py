from django.contrib import admin
from .models import (
    TaxRegion, OwnerAddress, Branches, EmployeeBasic, EmployeeContact, EmployeeAccess,
    EmployeeJob, Promotions, EmployeeHistory, EmployeeTermination,
    EmployeePayroll, EmployeeBank, EmployeeTax, EmployeeInsurance,
    EmployeeAttendance, EmployeePerformance, EmployeeLeave,
    EmployeeTrainingPrograms, EmployeeTrainingRecords
)

# --- INLINES (Display these INSIDE the Employee page) ---

class EmployeeContactInline(admin.StackedInline):
    model = EmployeeContact
    can_delete = False
    verbose_name_plural = 'Contact Details'

class EmployeeAccessInline(admin.StackedInline):
    model = EmployeeAccess
    can_delete = False
    verbose_name_plural = 'System Access & RFID'

class EmployeeBankInline(admin.StackedInline):
    model = EmployeeBank
    can_delete = False
    verbose_name_plural = 'Bank Information'

class EmployeeTaxInline(admin.StackedInline):
    model = EmployeeTax
    can_delete = False
    verbose_name_plural = 'Tax Information'

class EmployeeJobInline(admin.TabularInline):
    model = EmployeeJob
    fk_name = "employee"  # FIXED: Tells Django this inline belongs to the employee, not the manager
    extra = 0
    verbose_name_plural = 'Job History / Current Role'

# --- MAIN ADMIN CONFIGURATIONS ---

@admin.register(EmployeeBasic)
class EmployeeBasicAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_id', 'gender', 'dob')
    search_fields = ('first_name', 'last_name', 'national_id')
    list_filter = ('gender',)
    readonly_fields = ('gender',)
    inlines = [
        EmployeeContactInline,
        EmployeeAccessInline,
        EmployeeBankInline,
        EmployeeTaxInline,
        EmployeeJobInline,
    ]

@admin.register(OwnerAddress)
class OwnerAddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'town_area', 'city', 'is_rural_area')
    list_filter = ('city', 'is_rural_area')
    search_fields = ('street', 'town_area', 'city')

@admin.register(EmployeeAttendance)
class EmployeeAttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'attendance_date', 'check_in', 'check_out', 'status')
    list_filter = ('attendance_date', 'status', 'employee')
    date_hierarchy = 'attendance_date'

@admin.register(TaxRegion)
class TaxRegionAdmin(admin.ModelAdmin):
    list_display = ('city', 'province', 'tax_code')
    search_fields = ('city', 'tax_code')

@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    list_display = ('branch_name',)

@admin.register(EmployeeLeave)
class EmployeeLeaveAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'leave_type')

# --- STANDARD REGISTRATIONS ---

admin.site.register(Promotions)
admin.site.register(EmployeeHistory)
admin.site.register(EmployeeTermination)
admin.site.register(EmployeePayroll)
admin.site.register(EmployeeInsurance)
admin.site.register(EmployeePerformance)
admin.site.register(EmployeeTrainingPrograms)
admin.site.register(EmployeeTrainingRecords)