from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter
from .api_views import (
    FarmBasicViewSet, FarmLocationViewSet, FarmOwnershipViewSet,
    HousesViewSet, HouseSpecsViewSet, HouseUtilitiesViewSet,
    ConstructionProjectsViewSet, FarmAuditsViewSet
)# --- SETUP ROUTER ---
router = DefaultRouter()
router.register(r'farms', FarmBasicViewSet)
router.register(r'locations', FarmLocationViewSet)
router.register(r'ownerships', FarmOwnershipViewSet)
router.register(r'houses', HousesViewSet)
router.register(r'house-specs', HouseSpecsViewSet)
router.register(r'house-utilities', HouseUtilitiesViewSet)
router.register(r'projects', ConstructionProjectsViewSet)
router.register(r'audits', FarmAuditsViewSet)
urlpatterns = [
    # ==========================================
    # 1. GENERAL FARM INFO
    # ==========================================
    
    # Farm Basic (/farm/general/basic/)
    path('general/basic/', UniversalListView.as_view(), {'model_name': 'basic'}, name='farm_basic_list'),
    path('general/basic/add/', UniversalCreateView.as_view(), {'model_name': 'basic'}, name='farm_basic_create'),
    path('general/basic/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'basic'}, name='farm_basic_update'),
    path('general/basic/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'basic'}, name='farm_basic_delete'),

    # Location (/farm/general/location/)
    path('general/location/', UniversalListView.as_view(), {'model_name': 'location'}, name='farm_location_list'),
    path('general/location/add/', UniversalCreateView.as_view(), {'model_name': 'location'}, name='farm_location_create'),
    path('general/location/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'location'}, name='farm_location_update'),
    path('general/location/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'location'}, name='farm_location_delete'),

    # Ownership (/farm/general/ownership/)
    path('general/ownership/', UniversalListView.as_view(), {'model_name': 'ownership'}, name='farm_ownership_list'),
    path('general/ownership/add/', UniversalCreateView.as_view(), {'model_name': 'ownership'}, name='farm_ownership_create'),
    path('general/ownership/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'ownership'}, name='farm_ownership_update'),
    path('general/ownership/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'ownership'}, name='farm_ownership_delete'),

    # ==========================================
    # 2. HOUSING INFRASTRUCTURE
    # ==========================================

    # Houses (/farm/housing/houses/)
    path('housing/houses/', UniversalListView.as_view(), {'model_name': 'houses'}, name='farm_houses_list'),
    path('housing/houses/add/', UniversalCreateView.as_view(), {'model_name': 'houses'}, name='farm_houses_create'),
    path('housing/houses/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'houses'}, name='farm_houses_update'),
    path('housing/houses/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'houses'}, name='farm_houses_delete'),

    # Specs (/farm/housing/specs/)
    path('housing/specs/', UniversalListView.as_view(), {'model_name': 'specs'}, name='farm_specs_list'),
    path('housing/specs/add/', UniversalCreateView.as_view(), {'model_name': 'specs'}, name='farm_specs_create'),
    path('housing/specs/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'specs'}, name='farm_specs_update'),
    path('housing/specs/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'specs'}, name='farm_specs_delete'),

    # Utilities (/farm/housing/utilities/)
    path('housing/utilities/', UniversalListView.as_view(), {'model_name': 'utilities'}, name='farm_utilities_list'),
    path('housing/utilities/add/', UniversalCreateView.as_view(), {'model_name': 'utilities'}, name='farm_utilities_create'),
    path('housing/utilities/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'utilities'}, name='farm_utilities_update'),
    path('housing/utilities/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'utilities'}, name='farm_utilities_delete'),

    # ==========================================
    # 3. PROJECTS & AUDITS
    # ==========================================

    # Construction (/farm/projects/)
    path('projects/', UniversalListView.as_view(), {'model_name': 'construction'}, name='farm_construction_list'),
    path('projects/add/', UniversalCreateView.as_view(), {'model_name': 'construction'}, name='farm_construction_create'),
    path('projects/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'construction'}, name='farm_construction_update'),
    path('projects/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'construction'}, name='farm_construction_delete'),

    # Audits (/farm/audits/)
    path('audits/', UniversalListView.as_view(), {'model_name': 'audits'}, name='farm_audits_list'),
    path('audits/add/', UniversalCreateView.as_view(), {'model_name': 'audits'}, name='farm_audits_create'),
    path('audits/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'audits'}, name='farm_audits_update'),
    path('audits/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'audits'}, name='farm_audits_delete'),
    path('', include(router.urls)),
]