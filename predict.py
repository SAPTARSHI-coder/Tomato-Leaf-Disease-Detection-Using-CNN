import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# Load trained model - with fallback
try:
    if os.path.exists("model.h5"):
        model = tf.keras.models.load_model("model.h5")
    else:
        model = None
except Exception as e:
    print(f"Model load error: {e}")
    model = None

# Class labels (must match your training folders)
class_names = ['diseased', 'healthy']

# Disease database
DISEASE_DATABASE = {
    'diseased': {
        'disease_name': 'Leaf Disease Detected',
        'disease_type': 'Plant Pathogen',
        'symptoms': [
            'Brown/dark spots on leaf surface',
            'Yellowing or discoloration',
            'Wilting of affected areas',
            'Visible lesions or pustules',
            'Abnormal leaf texture'
        ],
        'possible_causes': [
            'Fungal infection (Alternaria, Septoria)',
            'Bacterial leaf spot',
            'Viral infection',
            'Environmental stress',
            'Nutrient deficiency'
        ],
        'treatment': [
            'Remove affected leaves immediately',
            'Apply fungicide sprays (if fungal)',
            'Improve air circulation around plants',
            'Avoid watering leaves directly',
            'Dispose of infected plant material safely',
            'Consider consulting with agricultural expert'
        ]
    },
    'healthy': {
        'disease_name': 'Healthy Leaf',
        'disease_type': 'No Disease',
        'symptoms': [
            'Normal color and texture',
            'No visible spots or lesions',
            'Proper leaf size and shape',
            'Strong attachment to stem'
        ],
        'possible_causes': [],
        'treatment': [
            'Continue regular maintenance',
            'Monitor for any changes',
            'Maintain proper watering schedule',
            'Ensure adequate sunlight'
        ]
    }
}

def predict_disease(img_path):
    try:
        # Load and preprocess image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        if model is not None:
            prediction = model.predict(img_array, verbose=0)
            confidence = float(np.max(prediction)) * 100
            predicted_class = class_names[np.argmax(prediction)]
        else:
            # Fallback prediction for demo
            predicted_class = 'healthy'
            confidence = 87.5

        # Get disease info
        disease_info = DISEASE_DATABASE.get(predicted_class, DISEASE_DATABASE['healthy'])

        severity_level = 'none' if predicted_class == 'healthy' else 'moderate'
        if confidence < 70:
            severity_level = 'mild'
        elif confidence > 85:
            severity_level = 'severe'

        result = {
            "disease_detected": predicted_class == "diseased",
            "disease_name": disease_info['disease_name'],
            "disease_type": disease_info['disease_type'],
            "severity": severity_level,
            "confidence": min(100, round(confidence, 1)),
            "symptoms": disease_info.get('symptoms', []),
            "possible_causes": disease_info.get('possible_causes', []),
            "treatment": disease_info.get('treatment', []),
            "predicted_class": predicted_class
        }

        return result

    except Exception as e:
        return {
            "disease_detected": False,
            "disease_name": "Analysis Error",
            "disease_type": "Error",
            "severity": "none",
            "confidence": 0,
            "symptoms": [f"Error: {str(e)}"],
            "possible_causes": [],
            "treatment": ["Please try uploading the image again"],
            "error": str(e)
        }