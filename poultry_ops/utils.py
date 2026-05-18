from django.apps import apps

def get_model_by_name(model_name):
    
    model_map = {
        'breeds': 'BirdBreeds',
        'batches': 'Batches',
        'mortality': 'MortalityRecords',
        'vaccines': 'Vaccines',
        'vaccine-records': 'VaccineRecords', 
        'vet': 'VetVisits',
        'eggs': 'EggCollection',
        'tasks': 'FarmTasks',
        'farmstatus':'FarmStatus',
    }
    
    class_name = model_map.get(model_name, model_name.capitalize())
    
    return apps.get_model('poultry_ops', class_name)