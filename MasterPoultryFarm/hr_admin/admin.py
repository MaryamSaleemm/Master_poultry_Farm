from django.contrib import admin
from .models import (
    OwnerAddress, Branches, EmployeeBasic, EmployeeContact, EmployeeAccess,
    EmployeeJob, Promotions, EmployeeHistory, EmployeeTermination,
    EmployeePayroll, EmployeeBank, EmployeeTax, EmployeeInsurance,
    EmployeeAttendance, EmployeePerformance, EmployeeLeave,
    EmployeeTrainingPrograms, EmployeeTrainingRecords
)

# --- Register all models ---
admin.site.register(OwnerAddress)
admin.site.register(Branches)
admin.site.register(EmployeeBasic)
admin.site.register(EmployeeContact)
admin.site.register(EmployeeAccess)
admin.site.register(EmployeeJob)
admin.site.register(Promotions)
admin.site.register(EmployeeHistory)
admin.site.register(EmployeeTermination)
admin.site.register(EmployeePayroll)
admin.site.register(EmployeeBank)
admin.site.register(EmployeeTax)
admin.site.register(EmployeeInsurance)
admin.site.register(EmployeeAttendance)
admin.site.register(EmployeePerformance)
admin.site.register(EmployeeLeave)
admin.site.register(EmployeeTrainingPrograms)
admin.site.register(EmployeeTrainingRecords)