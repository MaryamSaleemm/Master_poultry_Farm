from django.urls import path
from . import views
from .views import (
    HRDashboardView, UniversalListView, UniversalCreateView, 
    UniversalUpdateView, UniversalDeleteView
)

urlpatterns = [
    # DASHBOARD
    path('', HRDashboardView.as_view(), name='hr_dashboard'),
    path('dashboard/', HRDashboardView.as_view(), name='hr_dashboard_alias'),
    
    path('todo/', UniversalListView.as_view(), {'model_name': 'todo'}, name='todo_list'),
    path('todo/add/', UniversalCreateView.as_view(), {'model_name': 'todo'}, name='todo_create'),
    path('todo/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'todo'}, name='todo_update'),
    path('todo/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'todo'}, name='todo_delete'),
    path('api/add-todo/', views.add_todo, name='add_todo'),
    path('api/delete-todo/', views.delete_todo, name='delete_todo'),
    path('api/toggle-todo/', views.toggle_todo, name='toggle_todo'),
    
    #  CORE EMPLOYEE INFO
    
    path('employees/', UniversalListView.as_view(), {'model_name': 'basic'}, name='employee_basic_list'),
    path('employees/add/', UniversalCreateView.as_view(), {'model_name': 'basic'}, name='employee_basic_create'),
    path('employees/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'basic'}, name='employee_basic_update'),
    path('employees/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'basic'}, name='employee_basic_delete'),

    path('contact/', UniversalListView.as_view(), {'model_name': 'contact'}, name='employee_contact_list'),
    path('contact/add/', UniversalCreateView.as_view(), {'model_name': 'contact'}, name='employee_contact_create'),
    path('contact/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'contact'}, name='employee_contact_update'),
    path('contact/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'contact'}, name='employee_contact_delete'),

    path('access/', UniversalListView.as_view(), {'model_name': 'access'}, name='employee_access_list'),
    path('access/add/', UniversalCreateView.as_view(), {'model_name': 'access'}, name='employee_access_create'),
    path('access/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'access'}, name='employee_access_update'),
    path('access/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'access'}, name='employee_access_delete'),

    # JOB & CAREER

    path('jobs/', UniversalListView.as_view(), {'model_name': 'job'}, name='employee_job_list'),
    path('jobs/add/', UniversalCreateView.as_view(), {'model_name': 'job'}, name='employee_job_create'),
    path('jobs/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'job'}, name='employee_job_update'),
    path('jobs/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'job'}, name='employee_job_delete'),

    path('promotions/', UniversalListView.as_view(), {'model_name': 'promotion'}, name='promotions_list'),
    path('promotions/add/', UniversalCreateView.as_view(), {'model_name': 'promotion'}, name='promotions_create'),
    path('promotions/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'promotion'}, name='promotions_update'),
    path('promotions/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'promotion'}, name='promotions_delete'),

    path('history/', UniversalListView.as_view(), {'model_name': 'history'}, name='employee_history_list'),
    path('history/add/', UniversalCreateView.as_view(), {'model_name': 'history'}, name='employee_history_create'),
    path('history/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'history'}, name='employee_history_update'),
    path('history/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'history'}, name='employee_history_delete'),

    path('termination/', UniversalListView.as_view(), {'model_name': 'termination'}, name='employee_termination_list'),
    path('termination/add/', UniversalCreateView.as_view(), {'model_name': 'termination'}, name='employee_termination_create'),
    path('termination/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'termination'}, name='employee_termination_update'),
    path('termination/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'termination'}, name='employee_termination_delete'),

    # PAYROLL & FINANCE

    path('payroll/', UniversalListView.as_view(), {'model_name': 'payroll'}, name='employee_payroll_list'),
    path('payroll/add/', UniversalCreateView.as_view(), {'model_name': 'payroll'}, name='employee_payroll_create'),
    path('payroll/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'payroll'}, name='employee_payroll_update'),
    path('payroll/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'payroll'}, name='employee_payroll_delete'),

    path('bank/', UniversalListView.as_view(), {'model_name': 'bank'}, name='employee_bank_list'),
    path('bank/add/', UniversalCreateView.as_view(), {'model_name': 'bank'}, name='employee_bank_create'),
    path('bank/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'bank'}, name='employee_bank_update'),
    path('bank/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'bank'}, name='employee_bank_delete'),

    path('tax/', UniversalListView.as_view(), {'model_name': 'tax'}, name='employee_tax_list'),
    path('tax/add/', UniversalCreateView.as_view(), {'model_name': 'tax'}, name='employee_tax_create'),
    path('tax/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'tax'}, name='employee_tax_update'),
    path('tax/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'tax'}, name='employee_tax_delete'),

    path('insurance/', UniversalListView.as_view(), {'model_name': 'insurance'}, name='employee_insurance_list'),
    path('insurance/add/', UniversalCreateView.as_view(), {'model_name': 'insurance'}, name='employee_insurance_create'),
    path('insurance/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'insurance'}, name='employee_insurance_update'),
    path('insurance/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'insurance'}, name='employee_insurance_delete'),

    # OPERATIONS

    path('attendance/', UniversalListView.as_view(), {'model_name': 'attendance'}, name='employee_attendance_list'),
    path('attendance/add/', UniversalCreateView.as_view(), {'model_name': 'attendance'}, name='employee_attendance_create'),
    path('attendance/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'attendance'}, name='employee_attendance_update'),
    path('attendance/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'attendance'}, name='employee_attendance_delete'),

    path('performance/', UniversalListView.as_view(), {'model_name': 'performance'}, name='employee_performance_list'),
    path('performance/add/', UniversalCreateView.as_view(), {'model_name': 'performance'}, name='employee_performance_create'),
    path('performance/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'performance'}, name='employee_performance_update'),
    path('performance/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'performance'}, name='employee_performance_delete'),

    # Leaves 
    path('leave/', UniversalListView.as_view(), {'model_name': 'leave'}, name='employee_leave_list'),
    path('leave/add/', UniversalCreateView.as_view(), {'model_name': 'leave'}, name='employee_leave_create'),
    path('leave/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'leave'}, name='employee_leave_update'),
    path('leave/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'leave'}, name='employee_leave_delete'),

    # TRAINING

    path('training/programs/', UniversalListView.as_view(), {'model_name': 'training-programs'}, name='training_programs_list'),
    path('training/programs/add/', UniversalCreateView.as_view(), {'model_name': 'training-programs'}, name='training_programs_create'),
    path('training/programs/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'training-programs'}, name='training_programs_update'),
    path('training/programs/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'training-programs'}, name='training_programs_delete'),

    path('training/records/', UniversalListView.as_view(), {'model_name': 'training-records'}, name='training_records_list'),
    path('training/records/add/', UniversalCreateView.as_view(), {'model_name': 'training-records'}, name='training_records_create'),
    path('training/records/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'training-records'}, name='training_records_update'),
    path('training/records/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'training-records'}, name='training_records_delete'),

    # SETTINGS

    path('branches/', UniversalListView.as_view(), {'model_name': 'branches'}, name='branches_list'),
    path('branches/add/', UniversalCreateView.as_view(), {'model_name': 'branches'}, name='branches_create'),
    path('branches/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'branches'}, name='branches_update'),
    path('branches/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'branches'}, name='branches_delete'),

    path('addresses/', UniversalListView.as_view(), {'model_name': 'address'}, name='address_list'),
    path('addresses/add/', UniversalCreateView.as_view(), {'model_name': 'address'}, name='address_create'),
    path('addresses/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'address'}, name='address_update'),
    path('addresses/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'address'}, name='address_delete'),

    path('manage/<str:model_name>/', UniversalListView.as_view(), name='universal_list'),
    path('manage/<str:model_name>/add/', UniversalCreateView.as_view(), name='universal_create'),
    path('manage/<str:model_name>/<int:pk>/edit/', UniversalUpdateView.as_view(), name='universal_edit'),
    path('manage/<str:model_name>/<int:pk>/delete/', UniversalDeleteView.as_view(), name='universal_delete'),
    
   
]