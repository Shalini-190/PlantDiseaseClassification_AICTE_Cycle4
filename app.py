import os
import cv2
import numpy as np
import streamlit as st
import tensorflow as tf

# Check current working directory and files
print("Current Directory:", os.getcwd())
print("Files:", os.listdir())

# Load the trained model safely
try:
    model_path = os.path.abspath("my_model.keras")
  # Ensure absolute path
    print("Loading model from:", model_path)
    model = tf.keras.models.load_model(model_path)
except Exception as e:
    print("Error loading model:", e)
    st.error("Failed to load the model. Please check the file path and model compatibility.")
    model = None

# Define disease causes and solutions
disease_info = {
    'Powdery Mildew': {'cause': 'Humidity (Fungal Infection)', 'factor': 'Airborne', 'survival_days': 30, 'solution': 'Use fungicides, improve air circulation', 'treatment_possible': True},
    'Leaf Rust': {'cause': 'Fungal Spores in Soil', 'factor': 'Soil', 'survival_days': 40, 'solution': 'Apply fungicide, remove infected leaves', 'treatment_possible': True},
    'Bacterial Blight': {'cause': 'Water Contamination', 'factor': 'Water', 'survival_days': 20, 'solution': 'Use clean water, apply copper-based bactericide', 'treatment_possible': True},
    'Pest Infestation': {'cause': 'Pesticide Resistance', 'factor': 'Pesticides', 'survival_days': 25, 'solution': 'Introduce natural predators, rotate pesticides', 'treatment_possible': True},
    'Root Rot': {'cause': 'Excess Soil Moisture', 'factor': 'Soil', 'survival_days': 15, 'solution': 'Improve drainage, reduce watering', 'treatment_possible': False},
    'Anthracnose': {'cause': 'Fungal Infection in Warm Weather', 'factor': 'Airborne', 'survival_days': 35, 'solution': 'Apply copper fungicide, remove infected parts', 'treatment_possible': True},
    'Mosaic Virus': {'cause': 'Viral Infection through Insects', 'factor': 'Insects', 'survival_days': 50, 'solution': 'Use resistant plant varieties, control insect vectors', 'treatment_possible': False},
    'Late Blight': {'cause': 'Waterborne Fungal Spores', 'factor': 'Water', 'survival_days': 10, 'solution': 'Remove infected plants, apply fungicide', 'treatment_possible': False},
    'Downy Mildew': {'cause': 'High Humidity and Poor Ventilation', 'factor': 'Airborne', 'survival_days': 28, 'solution': 'Improve airflow, apply appropriate fungicides', 'treatment_possible': True},
    'Wilt Disease': {'cause': 'Soilborne Fungal Infection', 'factor': 'Soil', 'survival_days': 45, 'solution': 'Use disease-resistant varieties, rotate crops', 'treatment_possible': True}
}

# Function to predict disease and provide additional details
def predict_disease(image_path):
    try:
        img = cv2.imread(image_path)
        img = cv2.resize(img, (224, 224))
        img = np.expand_dims(img, axis=0) / 255.0
        
        prediction = model.predict(img)
        predicted_class = np.argmax(prediction)
        class_labels = list(disease_info.keys())
        
        if predicted_class >= len(class_labels):
            return {
                'Disease': 'Unknown Disease',
                'Cause': 'Not in database',
                'Factor': 'Unknown',
                'Estimated Survival': 'Unknown',
                'Solution': 'Consult an agricultural expert',
                'Treatment Possible': 'Unknown',
                'Recommendation': 'Further diagnosis needed'
            }
        
        disease_name = class_labels[predicted_class]
        info = disease_info[disease_name]
        
        recommendation = 'Remove the plant' if not info['treatment_possible'] else 'Apply treatment'
        
        return {
            'Disease': disease_name,
            'Cause': info['cause'],
            'Factor': info['factor'],
            'Estimated Survival': f"{info['survival_days']} days",
            'Solution': info['solution'],
            'Treatment Possible': 'Yes' if info['treatment_possible'] else 'No',
            'Recommendation': recommendation
        }
    except Exception as e:
        print("Error during prediction:", e)
        return {'Disease': 'Error', 'Solution': 'Prediction failed. Check input image and model.'}

# Streamlit UI
st.sidebar.title('Plant Disease Prediction System')
st.sidebar.markdown('Upload an image to detect plant disease and get recommendations.')

st.markdown("<h1 style='text-align: center;'>Plant Disease Prediction System</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a plant leaf image", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    image_path = "temp.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Predict Disease") and model:
        result = predict_disease(image_path)
        
        st.write(f"**Disease:** {result['Disease']}")
        st.write(f"**Cause:** {result['Cause']}")
        st.write(f"**Factor:** {result['Factor']}")
        st.write(f"**Estimated Survival:** {result['Estimated Survival']}")
        st.write(f"**Solution:** {result['Solution']}")
        st.write(f"**Treatment Possible:** {result['Treatment Possible']}")
        st.write(f"**Recommendation:** {result['Recommendation']}")
