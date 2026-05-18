import os
import joblib
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

MODELS_DIR = os.path.join(CURRENT_DIR, 'ml_models')

def load_model(filename):
    path = os.path.join(MODELS_DIR, filename)
    if os.path.exists(path):
        try:
            return joblib.load(path)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return None
    else:
        print(f"CRITICAL WARNING: File not found at: {path}") 
        return None


egg_model = load_model('egg_model.pkl')
feed_model = load_model('feed_prediction_model.pkl')
env_model = load_model('environment_monitor_model.pkl')



def ai_dashboard(request):
    return render(request, 'ai_dashboard.html', {})


def predict_eggs_api(request):
    """
    Egg Model: Expecting 4 Features -> [Feed, Temp, Humidity, Breed]
    """
    if request.method == 'POST':
        try:
            feed = float(request.POST.get('feed_kg', 0))
            temp = float(request.POST.get('temp_c', 0))
            hum = float(request.POST.get('humidity', 0))
            
           
            breed_map = {'1': 0, '2': 1, '3': 2} 
            breed = breed_map.get(request.POST.get('breed_type'), 0)

            if egg_model:
                
                input_data = np.array([[feed, temp, hum, breed]])
                prediction = egg_model.predict(input_data)[0]
                
                return JsonResponse({
                    'status': 'success', 
                    'prediction': int(prediction), 
                    'unit': 'eggs'
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'egg_model.pkl not found'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def predict_feed_api(request):
    """
    Feed Model: Expecting 4 Features -> [FeedType, Formula, Temp, Season]
    """
    if request.method == 'POST':
        try:
            
            f_type_map = {'Starter': 0, 'Grower': 1, 'Layer': 2}
            formula_map = {'Standard': 0, 'HighPro': 1, 'Organic': 2} 
            season_map = {'Spring': 0, 'Summer': 1, 'Autumn': 2, 'Winter': 3}
            
            f_type = f_type_map.get(request.POST.get('feed_type'), 2)
            formula = formula_map.get(request.POST.get('blend_formula'), 0) 
            temp = float(request.POST.get('avg_temp', 25))
            season = season_map.get(request.POST.get('season'), 0)

            if feed_model:
               
                input_data = np.array([[f_type, formula, temp, season]])
                
                prediction = feed_model.predict(input_data)[0]
                
                return JsonResponse({
                    'status': 'success', 
                    'prediction': round(prediction, 2), 
                    'unit': 'kg'
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'feed_prediction_model.pkl not found'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def monitor_env_api(request):
    """
    Env Model: Expecting 3 Features -> [Temp, Humidity, ExtraFeature]
    """
    if request.method == 'POST':
        try:
            temp = float(request.POST.get('temp_c', 0))
            hum = float(request.POST.get('humidity_pct', 0))
            
            
            extra_feature = 0 

            if env_model:
                
                input_data = np.array([[temp, hum, extra_feature]])
                
                prediction = env_model.predict(input_data)[0]
                
                
                status = str(prediction)
                if status == '0': status = "Safe"
                elif status == '1': status = "Warning"
                elif status == '2': status = "Critical"

                return JsonResponse({
                    'status': 'success', 
                    'prediction': status, 
                    'unit': 'status'
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'environment_monitor_model.pkl not found'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})