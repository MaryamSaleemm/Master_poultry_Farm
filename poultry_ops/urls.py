from django.urls import path
from .views import (
    UniversalListView, UniversalCreateView, 
    UniversalUpdateView, UniversalDeleteView
)

urlpatterns = [
    # FLOCK MANAGEMENT
    
    # Breeds
    path('flock/breeds/', UniversalListView.as_view(), {'model_name': 'breeds'}, name='poultry_breeds_list'),
    path('flock/breeds/add/', UniversalCreateView.as_view(), {'model_name': 'breeds'}, name='poultry_breeds_create'),
    path('flock/breeds/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'breeds'}, name='poultry_breeds_update'),
    path('flock/breeds/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'breeds'}, name='poultry_breeds_delete'),

    # Batches
    path('flock/batches/', UniversalListView.as_view(), {'model_name': 'batches'}, name='poultry_batches_list'),
    path('flock/batches/add/', UniversalCreateView.as_view(), {'model_name': 'batches'}, name='poultry_batches_create'),
    path('flock/batches/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'batches'}, name='poultry_batches_update'),
    path('flock/batches/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'batches'}, name='poultry_batches_delete'),

    # Mortality
    path('flock/mortality/', UniversalListView.as_view(), {'model_name': 'mortality'}, name='poultry_mortality_list'),
    path('flock/mortality/add/', UniversalCreateView.as_view(), {'model_name': 'mortality'}, name='poultry_mortality_create'),
    path('flock/mortality/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'mortality'}, name='poultry_mortality_update'),
    path('flock/mortality/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'mortality'}, name='poultry_mortality_delete'),

    # HEALTH MANAGEMENT

    # Vaccines
    path('health/vaccines/', UniversalListView.as_view(), {'model_name': 'vaccines'}, name='poultry_vaccines_list'),
    path('health/vaccines/add/', UniversalCreateView.as_view(), {'model_name': 'vaccines'}, name='poultry_vaccines_create'),
    path('health/vaccines/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'vaccines'}, name='poultry_vaccines_update'),
    path('health/vaccines/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'vaccines'}, name='poultry_vaccines_delete'),

    # Vaccine Records
    path('health/records/', UniversalListView.as_view(), {'model_name': 'vaccine-records'}, name='poultry_vaccinerecords_list'),
    path('health/records/add/', UniversalCreateView.as_view(), {'model_name': 'vaccine-records'}, name='poultry_vaccinerecords_create'),
    path('health/records/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'vaccine-records'}, name='poultry_vaccinerecords_update'),
    path('health/records/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'vaccine-records'}, name='poultry_vaccinerecords_delete'),

    # Vet Visits
    path('health/vet/', UniversalListView.as_view(), {'model_name': 'vet'}, name='poultry_vet_list'),
    path('health/vet/add/', UniversalCreateView.as_view(), {'model_name': 'vet'}, name='poultry_vet_create'),
    path('health/vet/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'vet'}, name='poultry_vet_update'),
    path('health/vet/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'vet'}, name='poultry_vet_delete'),

    # PRODUCTION & OPERATIONS

    # Egg Collection
    path('production/eggs/', UniversalListView.as_view(), {'model_name': 'eggs'}, name='poultry_eggs_list'),
    path('production/eggs/add/', UniversalCreateView.as_view(), {'model_name': 'eggs'}, name='poultry_eggs_create'),
    path('production/eggs/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'eggs'}, name='poultry_eggs_update'),
    path('production/eggs/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'eggs'}, name='poultry_eggs_delete'),

    path('tasks/', UniversalListView.as_view(), {'model_name': 'tasks'}, name='poultry_tasks_list'),
    path('tasks/add/', UniversalCreateView.as_view(), {'model_name': 'tasks'}, name='poultry_tasks_create'),
    path('tasks/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'tasks'}, name='poultry_tasks_update'),
    path('tasks/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'tasks'}, name='poultry_tasks_delete'),
    
    path('status/', UniversalListView.as_view(), {'model_name': 'farmstatus'}, name='poultry_farmstatus_list'),
    path('status/add/', UniversalCreateView.as_view(), {'model_name': 'farmstatus'}, name='poultry_farmstatus_create'),
    path('status/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'farmstatus'}, name='poultry_farmstatus_update'),
    path('status/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'farmstatus'}, name='poultry_farmstatus_delete'),
]