from django.urls import path
from .views import (
    UniversalListView, UniversalCreateView, 
    UniversalUpdateView, UniversalDeleteView
)

urlpatterns = [
    #GENERAL FARM INFO
    
    path('general/basic/', UniversalListView.as_view(), {'model_name': 'basic'}, name='farm_basic_list'),
    path('general/basic/add/', UniversalCreateView.as_view(), {'model_name': 'basic'}, name='farm_basic_create'),
    path('general/basic/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'basic'}, name='farm_basic_update'),
    path('general/basic/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'basic'}, name='farm_basic_delete'),

    path('general/location/', UniversalListView.as_view(), {'model_name': 'location'}, name='farm_location_list'),
    path('general/location/add/', UniversalCreateView.as_view(), {'model_name': 'location'}, name='farm_location_create'),
    path('general/location/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'location'}, name='farm_location_update'),
    path('general/location/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'location'}, name='farm_location_delete'),

    path('general/ownership/', UniversalListView.as_view(), {'model_name': 'ownership'}, name='farm_ownership_list'),
    path('general/ownership/add/', UniversalCreateView.as_view(), {'model_name': 'ownership'}, name='farm_ownership_create'),
    path('general/ownership/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'ownership'}, name='farm_ownership_update'),
    path('general/ownership/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'ownership'}, name='farm_ownership_delete'),

    #HOUSING INFRASTRUCTURE

    path('housing/houses/', UniversalListView.as_view(), {'model_name': 'houses'}, name='farm_houses_list'),
    path('housing/houses/add/', UniversalCreateView.as_view(), {'model_name': 'houses'}, name='farm_houses_create'),
    path('housing/houses/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'houses'}, name='farm_houses_update'),
    path('housing/houses/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'houses'}, name='farm_houses_delete'),

    path('housing/specs/', UniversalListView.as_view(), {'model_name': 'specs'}, name='farm_specs_list'),
    path('housing/specs/add/', UniversalCreateView.as_view(), {'model_name': 'specs'}, name='farm_specs_create'),
    path('housing/specs/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'specs'}, name='farm_specs_update'),
    path('housing/specs/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'specs'}, name='farm_specs_delete'),

    path('housing/utilities/', UniversalListView.as_view(), {'model_name': 'utilities'}, name='farm_utilities_list'),
    path('housing/utilities/add/', UniversalCreateView.as_view(), {'model_name': 'utilities'}, name='farm_utilities_create'),
    path('housing/utilities/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'utilities'}, name='farm_utilities_update'),
    path('housing/utilities/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'utilities'}, name='farm_utilities_delete'),

    # 3. PROJECTS & AUDITS

    path('projects/', UniversalListView.as_view(), {'model_name': 'construction'}, name='farm_construction_list'),
    path('projects/add/', UniversalCreateView.as_view(), {'model_name': 'construction'}, name='farm_construction_create'),
    path('projects/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'construction'}, name='farm_construction_update'),
    path('projects/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'construction'}, name='farm_construction_delete'),

    path('audits/', UniversalListView.as_view(), {'model_name': 'audits'}, name='farm_audits_list'),
    path('audits/add/', UniversalCreateView.as_view(), {'model_name': 'audits'}, name='farm_audits_create'),
    path('audits/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'audits'}, name='farm_audits_update'),
    path('audits/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'audits'}, name='farm_audits_delete'),
]