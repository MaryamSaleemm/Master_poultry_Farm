from .models import (
    OwnerBasic, OwnerContact, OwnerAddress,
    BuildingBasic, BuildingLocation, BuildingSpecs, BuildingFacilities, BuildingManagement,
    Permits, Licenses, BuildingInspections
)

MODEL_MAP = {
    # Owners
    'owners': OwnerBasic,
    'owner-contacts': OwnerContact,
    'owner-address': OwnerAddress,
    
    # Buildings
    'buildings': BuildingBasic,
    'locations': BuildingLocation,
    'specs': BuildingSpecs,
    'facilities': BuildingFacilities,
    'management': BuildingManagement,

    # Compliance
    'permits': Permits,
    'licenses': Licenses,
    'inspections': BuildingInspections,
}

def get_model_by_name(name):
    """
    Retrieves a Django model class based on its lookup name defined in MODEL_MAP.
    """
    return MODEL_MAP.get(name)