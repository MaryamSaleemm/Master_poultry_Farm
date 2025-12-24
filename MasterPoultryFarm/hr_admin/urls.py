from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .api_views import EmployeeBasicViewSet, EmployeeJobViewSet # Import the API Views
from .api_views import DashboardStatsAPI, EmployeeBasicViewSet, EmployeeJobViewSet
from .api_views import (
    EmployeeBasicViewSet, EmployeeJobViewSet, EmployeeContactViewSet, 
    EmployeeAccessViewSet, OwnerAddressViewSet, EmployeeAttendanceViewSet,
    EmployeeLeaveViewSet, EmployeePerformanceViewSet, PromotionsViewSet,
    EmployeeHistoryViewSet, EmployeePayrollViewSet, EmployeeTrainingProgramsViewSet,
    EmployeeTrainingRecordsViewSet, BranchesViewSet
)
# In your urls.py

# 1. SETUP THE API ROUTER
router = DefaultRouter()

# --- Core Employee ---
router.register(r'employees', EmployeeBasicViewSet)
router.register(r'jobs', EmployeeJobViewSet)
router.register(r'contacts', EmployeeContactViewSet) # You need to import this
router.register(r'access', EmployeeAccessViewSet)    # You need to import this
router.register(r'addresses', OwnerAddressViewSet)   # You need to import this

# --- Operations ---
router.register(r'attendance', EmployeeAttendanceViewSet)
router.register(r'leaves', EmployeeLeaveViewSet)

# --- Performance ---
router.register(r'performance', EmployeePerformanceViewSet)
router.register(r'promotions', PromotionsViewSet)
router.register(r'history', EmployeeHistoryViewSet)

# --- Payroll & Training ---
router.register(r'payroll', EmployeePayrollViewSet)
router.register(r'training-programs', EmployeeTrainingProgramsViewSet)
router.register(r'training-records', EmployeeTrainingRecordsViewSet)

# --- Other ---
router.register(r'branches', BranchesViewSet)

urlpatterns = [
    # --- DASHBOARD ---
    path('', HRDashboardView.as_view(), name='hr_dashboard'),

    # ==========================================
    # 1. CORE EMPLOYEE INFO
    # ==========================================
    
    # Employee Basic (/employees/)
    path('employees/', UniversalListView.as_view(), {'model_name': 'basic'}, name='employee_basic_list'),
    path('employees/add/', UniversalCreateView.as_view(), {'model_name': 'basic'}, name='employee_basic_create'),
    path('employees/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'basic'}, name='employee_basic_update'),
    path('employees/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'basic'}, name='employee_basic_delete'),

    # Contact Details (/contact/)
    path('contact/', UniversalListView.as_view(), {'model_name': 'contact'}, name='employee_contact_list'),
    path('contact/add/', UniversalCreateView.as_view(), {'model_name': 'contact'}, name='employee_contact_create'),
    path('contact/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'contact'}, name='employee_contact_update'),
    path('contact/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'contact'}, name='employee_contact_delete'),

    # Access & Roles (/access/)
    path('access/', UniversalListView.as_view(), {'model_name': 'access'}, name='employee_access_list'),
    path('access/add/', UniversalCreateView.as_view(), {'model_name': 'access'}, name='employee_access_create'),
    path('access/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'access'}, name='employee_access_update'),
    path('access/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'access'}, name='employee_access_delete'),

    # ==========================================
    # 2. JOB & CAREER
    # ==========================================

    # Jobs (/jobs/)
    path('jobs/', UniversalListView.as_view(), {'model_name': 'job'}, name='employee_job_list'),
    path('jobs/add/', UniversalCreateView.as_view(), {'model_name': 'job'}, name='employee_job_create'),
    path('jobs/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'job'}, name='employee_job_update'),
    path('jobs/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'job'}, name='employee_job_delete'),

    # Promotions (/promotions/)
    path('promotions/', UniversalListView.as_view(), {'model_name': 'promotion'}, name='promotions_list'),
    path('promotions/add/', UniversalCreateView.as_view(), {'model_name': 'promotion'}, name='promotions_create'),
    path('promotions/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'promotion'}, name='promotions_update'),
    path('promotions/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'promotion'}, name='promotions_delete'),

    # History Logs (/history/)
    path('history/', UniversalListView.as_view(), {'model_name': 'history'}, name='employee_history_list'),
    path('history/add/', UniversalCreateView.as_view(), {'model_name': 'history'}, name='employee_history_create'),
    path('history/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'history'}, name='employee_history_update'),
    path('history/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'history'}, name='employee_history_delete'),

    # Terminations (/termination/)
    path('termination/', UniversalListView.as_view(), {'model_name': 'termination'}, name='employee_termination_list'),
    path('termination/add/', UniversalCreateView.as_view(), {'model_name': 'termination'}, name='employee_termination_create'),
    path('termination/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'termination'}, name='employee_termination_update'),
    path('termination/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'termination'}, name='employee_termination_delete'),

    # ==========================================
    # 3. PAYROLL & FINANCE
    # ==========================================

    # Payroll Setup (/payroll/)
    path('payroll/', UniversalListView.as_view(), {'model_name': 'payroll'}, name='employee_payroll_list'),
    path('payroll/add/', UniversalCreateView.as_view(), {'model_name': 'payroll'}, name='employee_payroll_create'),
    path('payroll/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'payroll'}, name='employee_payroll_update'),
    path('payroll/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'payroll'}, name='employee_payroll_delete'),

    # Bank Accounts (/bank/)
    path('bank/', UniversalListView.as_view(), {'model_name': 'bank'}, name='employee_bank_list'),
    path('bank/add/', UniversalCreateView.as_view(), {'model_name': 'bank'}, name='employee_bank_create'),
    path('bank/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'bank'}, name='employee_bank_update'),
    path('bank/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'bank'}, name='employee_bank_delete'),

    # Tax Info (/tax/)
    path('tax/', UniversalListView.as_view(), {'model_name': 'tax'}, name='employee_tax_list'),
    path('tax/add/', UniversalCreateView.as_view(), {'model_name': 'tax'}, name='employee_tax_create'),
    path('tax/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'tax'}, name='employee_tax_update'),
    path('tax/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'tax'}, name='employee_tax_delete'),

    # Insurance (/insurance/)
    path('insurance/', UniversalListView.as_view(), {'model_name': 'insurance'}, name='employee_insurance_list'),
    path('insurance/add/', UniversalCreateView.as_view(), {'model_name': 'insurance'}, name='employee_insurance_create'),
    path('insurance/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'insurance'}, name='employee_insurance_update'),
    path('insurance/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'insurance'}, name='employee_insurance_delete'),

    # ==========================================
    # 4. OPERATIONS
    # ==========================================

    # Attendance (/attendance/)
    path('attendance/', UniversalListView.as_view(), {'model_name': 'attendance'}, name='employee_attendance_list'),
    path('attendance/add/', UniversalCreateView.as_view(), {'model_name': 'attendance'}, name='employee_attendance_create'),
    path('attendance/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'attendance'}, name='employee_attendance_update'),
    path('attendance/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'attendance'}, name='employee_attendance_delete'),

    # Performance (/performance/)
    path('performance/', UniversalListView.as_view(), {'model_name': 'performance'}, name='employee_performance_list'),
    path('performance/add/', UniversalCreateView.as_view(), {'model_name': 'performance'}, name='employee_performance_create'),
    path('performance/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'performance'}, name='employee_performance_update'),
    path('performance/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'performance'}, name='employee_performance_delete'),

    # Leaves (/leave/)
    path('leave/', UniversalListView.as_view(), {'model_name': 'leave'}, name='employee_leave_list'),
    path('leave/add/', UniversalCreateView.as_view(), {'model_name': 'leave'}, name='employee_leave_create'),
    path('leave/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'leave'}, name='employee_leave_update'),
    path('leave/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'leave'}, name='employee_leave_delete'),

    # ==========================================
    # 5. TRAINING
    # ==========================================

    # Programs (/training/programs/)
    path('training/programs/', UniversalListView.as_view(), {'model_name': 'training-programs'}, name='training_programs_list'),
    path('training/programs/add/', UniversalCreateView.as_view(), {'model_name': 'training-programs'}, name='training_programs_create'),
    path('training/programs/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'training-programs'}, name='training_programs_update'),
    path('training/programs/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'training-programs'}, name='training_programs_delete'),

    # Records (/training/records/)
    path('training/records/', UniversalListView.as_view(), {'model_name': 'training-records'}, name='training_records_list'),
    path('training/records/add/', UniversalCreateView.as_view(), {'model_name': 'training-records'}, name='training_records_create'),
    path('training/records/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'training-records'}, name='training_records_update'),
    path('training/records/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'training-records'}, name='training_records_delete'),

    # ==========================================
    # 6. SETTINGS
    # ==========================================

    # Branches (/branches/)
    path('branches/', UniversalListView.as_view(), {'model_name': 'branches'}, name='branches_list'),
    path('branches/add/', UniversalCreateView.as_view(), {'model_name': 'branches'}, name='branches_create'),
    path('branches/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'branches'}, name='branches_update'),
    path('branches/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'branches'}, name='branches_delete'),

    # Addresses (/addresses/)
    path('addresses/', UniversalListView.as_view(), {'model_name': 'address'}, name='address_list'),
    path('addresses/add/', UniversalCreateView.as_view(), {'model_name': 'address'}, name='address_create'),
    path('addresses/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'address'}, name='address_update'),
    path('addresses/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'address'}, name='address_delete'),

    # --- FALLBACK (Required for Add/Edit buttons to work) ---
    path('manage/<str:model_name>/', UniversalListView.as_view(), name='universal_list'),
    path('manage/<str:model_name>/add/', UniversalCreateView.as_view(), name='universal_create'),
    path('manage/<str:model_name>/<int:pk>/edit/', UniversalUpdateView.as_view(), name='universal_edit'),
    path('manage/<str:model_name>/<int:pk>/delete/', UniversalDeleteView.as_view(), name='universal_delete'),
    
    path('api/', include(router.urls)), 
    path('api/dashboard-stats/', DashboardStatsAPI.as_view(), name='api_dashboard_stats'), 
]