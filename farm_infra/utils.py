from .models import *

MODEL_MAP = {
    'basic': FarmBasic,
    'location': FarmLocation,
    'ownership': FarmOwnership,
    'houses': Houses,
    'specs': HouseSpecs,
    'utilities': HouseUtilities,
    'construction': ConstructionProjects,
    'audits': FarmAudits,
}

def get_model_by_name(name):
    return MODEL_MAP.get(name)