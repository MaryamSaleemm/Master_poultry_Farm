from django.urls import path
from .views import (
    UniversalListView, UniversalCreateView, 
    UniversalUpdateView, UniversalDeleteView
)

urlpatterns = [
    # 1. OWNER MANAGEMENT
    
    path('owners/basic/', UniversalListView.as_view(), {'model_name': 'owners'}, name='assets_owners_list'),
    path('owners/basic/add/', UniversalCreateView.as_view(), {'model_name': 'owners'}, name='assets_owners_create'),
    path('owners/basic/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'owners'}, name='assets_owners_update'),
    path('owners/basic/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'owners'}, name='assets_owners_delete'),

    path('owners/contact/', UniversalListView.as_view(), {'model_name': 'owner-contacts'}, name='assets_owner-contacts_list'),
    path('owners/contact/add/', UniversalCreateView.as_view(), {'model_name': 'owner-contacts'}, name='assets_owner-contacts_create'),
    path('owners/contact/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'owner-contacts'}, name='assets_owner-contacts_update'),
    path('owners/contact/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'owner-contacts'}, name='assets_owner-contacts_delete'),

    path('owners/address/', UniversalListView.as_view(), {'model_name': 'owner-address'}, name='assets_owner-address_list'),
    path('owners/address/add/', UniversalCreateView.as_view(), {'model_name': 'owner-address'}, name='assets_owner-address_create'),
    path('owners/address/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'owner-address'}, name='assets_owner-address_update'),
    path('owners/address/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'owner-address'}, name='assets_owner-address_delete'),

    
    # 2. BUILDING MANAGEMENT (Django HTML Views)
    
    path('buildings/basic/', UniversalListView.as_view(), {'model_name': 'buildings'}, name='assets_buildings_list'),
    path('buildings/basic/add/', UniversalCreateView.as_view(), {'model_name': 'buildings'}, name='assets_buildings_create'),
    path('buildings/basic/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'buildings'}, name='assets_buildings_update'),
    path('buildings/basic/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'buildings'}, name='assets_buildings_delete'),

    path('buildings/location/', UniversalListView.as_view(), {'model_name': 'locations'}, name='assets_locations_list'),
    path('buildings/location/add/', UniversalCreateView.as_view(), {'model_name': 'locations'}, name='assets_locations_create'),
    path('buildings/location/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'locations'}, name='assets_locations_update'),
    path('buildings/location/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'locations'}, name='assets_locations_delete'),

    path('buildings/specs/', UniversalListView.as_view(), {'model_name': 'specs'}, name='assets_specs_list'),
    path('buildings/specs/add/', UniversalCreateView.as_view(), {'model_name': 'specs'}, name='assets_specs_create'),
    path('buildings/specs/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'specs'}, name='assets_specs_update'),
    path('buildings/specs/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'specs'}, name='assets_specs_delete'),

    path('buildings/facilities/', UniversalListView.as_view(), {'model_name': 'facilities'}, name='assets_facilities_list'),
    path('buildings/facilities/add/', UniversalCreateView.as_view(), {'model_name': 'facilities'}, name='assets_facilities_create'),
    path('buildings/facilities/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'facilities'}, name='assets_facilities_update'),
    path('buildings/facilities/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'facilities'}, name='assets_facilities_delete'),

    path('buildings/management/', UniversalListView.as_view(), {'model_name': 'management'}, name='assets_management_list'),
    path('buildings/management/add/', UniversalCreateView.as_view(), {'model_name': 'management'}, name='assets_management_create'),
    path('buildings/management/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'management'}, name='assets_management_update'),
    path('buildings/management/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'management'}, name='assets_management_delete'),

    
    # 3. COMPLIANCE & LEGAL (Django HTML Views)
    
    path('compliance/permits/', UniversalListView.as_view(), {'model_name': 'permits'}, name='assets_permits_list'),
    path('compliance/permits/add/', UniversalCreateView.as_view(), {'model_name': 'permits'}, name='assets_permits_create'),
    path('compliance/permits/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'permits'}, name='assets_permits_update'),
    path('compliance/permits/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'permits'}, name='assets_permits_delete'),

    path('compliance/licenses/', UniversalListView.as_view(), {'model_name': 'licenses'}, name='assets_licenses_list'),
    path('compliance/licenses/add/', UniversalCreateView.as_view(), {'model_name': 'licenses'}, name='assets_licenses_create'),
    path('compliance/licenses/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'licenses'}, name='assets_licenses_update'),
    path('compliance/licenses/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'licenses'}, name='assets_licenses_delete'),

    path('compliance/inspections/', UniversalListView.as_view(), {'model_name': 'inspections'}, name='assets_inspections_list'),
    path('compliance/inspections/add/', UniversalCreateView.as_view(), {'model_name': 'inspections'}, name='assets_inspections_create'),
    path('compliance/inspections/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'inspections'}, name='assets_inspections_update'),
    path('compliance/inspections/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'inspections'}, name='assets_inspections_delete'),

    # FALLBACK
    path('manage/<str:model_name>/', UniversalListView.as_view(), name='assets_universal_list'),
]