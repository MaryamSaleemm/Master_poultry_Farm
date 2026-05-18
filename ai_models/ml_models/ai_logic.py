import os
import joblib
import pandas as pd
import numpy as np

# Define the base directory where .pkl files are located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Global cache for models
_MODELS = {}

def _load_resources():
    """Loads all models and encoders into memory if not already loaded."""
    global _MODELS
    if not _MODELS:
        try:
            # Load Egg Model & Encoder
            _MODELS['egg_model'] = joblib.load(os.path.join(BASE_DIR, 'egg_model.pkl'))
            _MODELS['egg_encoder'] = joblib.load(os.path.join(BASE_DIR, 'egg_label_encoder.pkl'))

            # Load Environment Model & Encoders (Dictionary)
            _MODELS['env_model'] = joblib.load(os.path.join(BASE_DIR, 'environment_monitor_model.pkl'))
            _MODELS['env_encoders'] = joblib.load(os.path.join(BASE_DIR, 'env_label_encoders.pkl'))

            # Load Feed Model & Encoders (Dictionary)
            _MODELS['feed_model'] = joblib.load(os.path.join(BASE_DIR, 'feed_prediction_model.pkl'))
            _MODELS['feed_encoders'] = joblib.load(os.path.join(BASE_DIR, 'feed_label_encoders.pkl'))

            print("✅ All AI Models loaded successfully via Joblib!")
        except Exception as e:
            print(f"❌ Error loading models: {e}")
            raise e

def predict_eggs_logic(feed_kg, temp_c, humidity, breed_type_input):
    """
    Predicts Egg Count based on your training script features.
    """
    _load_resources()
    
    # Encode Breed Type (Handle strings or raw codes)
    try:
        # If input is string (e.g., "Leghorn"), transform it. If numeric, keep it.
        if isinstance(breed_type_input, str) and not breed_type_input.isdigit():
             breed_encoded = _MODELS['egg_encoder'].transform([breed_type_input])[0]
        else:
             breed_encoded = int(breed_type_input)
    except:
        # Fallback: Default to 0 if unknown label
        breed_encoded = 0

    # Prepare DataFrame exactly as your training script expects
    input_data = pd.DataFrame({
        "Feed_kg": [float(feed_kg)],
        "Temperature_C": [float(temp_c)],
        "Humidity_%": [float(humidity)],
        "Breed_Type": [breed_encoded]
    })

    prediction = _MODELS['egg_model'].predict(input_data)
    return round(prediction[0])

def monitor_environment_logic(sensor_id_input, temp_c, humidity_pct):
    """
    Predicts Alert Status (Safe/Risk).
    """
    _load_resources()
    encoders = _MODELS['env_encoders']

    # Encode Sensor ID
    try:
        sensor_encoded = encoders['Sensor_ID'].transform([sensor_id_input])[0]
    except:
        sensor_encoded = 0 # Default fallback

    input_data = pd.DataFrame({
        "Sensor_ID": [sensor_encoded],
        "Temperature_C": [float(temp_c)],
        "Humidity_Pct": [float(humidity_pct)]
    })

    prediction_idx = _MODELS['env_model'].predict(input_data)[0]
    
    # Decode the result (0/1 -> "Normal"/"Critical")
    result_label = encoders['Alert_Status'].inverse_transform([prediction_idx])[0]
    return result_label

def predict_feed_logic(feed_type, blend_formula, avg_temp, season):
    """
    Predicts Daily Feed Amount (kg).
    """
    _load_resources()
    encoders = _MODELS['feed_encoders']

    # Helper to safe encode
    def safe_encode(encoder, value):
        try:
            return encoder.transform([value])[0]
        except:
            return 0 

    input_data = pd.DataFrame({
        "Feed_Type": [safe_encode(encoders['Feed_Type'], feed_type)],
        "Feed_Blend_Formula": [safe_encode(encoders['Feed_Blend_Formula'], blend_formula)],
        "Avg_House_Temp_C": [float(avg_temp)],
        "Season_Applied": [safe_encode(encoders['Season_Applied'], season)]
    })

    prediction = _MODELS['feed_model'].predict(input_data)
    return round(prediction[0], 2)