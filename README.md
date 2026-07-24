# Plant Disease Classification

Deep learning model for identifying plant diseases from leaf images. Built as part of the AICTE Internship Cycle 4.

## Overview

This project uses a Convolutional Neural Network (CNN) trained on the New Plant Diseases Dataset from Kaggle to classify plant leaves as healthy or diseased across multiple crop and disease categories.

## Features

- **Multi-class Classification** — Identifies 38 plant-disease categories
- **Streamlit Web App** — Simple UI for uploading and classifying leaf images
- **Trained Keras Model** — Pre-trained model ready for inference
- **Dataset** — 87K images across 38 classes from Kaggle

## Model

- Architecture: CNN (Keras/TensorFlow)
- Training dataset: [New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
- Pre-trained model: [Download from Google Drive](https://drive.google.com/file/d/1-J1Wo_SkN0eNdxD0yexQ3PkahI3Pi88V/view?usp=sharing)

## Tech Stack

- Python, TensorFlow/Keras
- Streamlit (web deployment)
- Jupyter Notebooks (training and experimentation)

## Getting Started

```bash
git clone https://github.com/Shalini-190/PlantDiseaseClassification_AICTE_Cycle4.git
cd PlantDiseaseClassification_AICTE_Cycle4
pip install -r requirements.txt
streamlit run app.py
```

## Project Files

- `Plant_Disease_Detection.ipynb` — Model training notebook
- `streamlit.ipynb` — Streamlit deployment notebook
- `app.py` — Streamlit web application
- `my_model.keras` — Trained model weights
- `requirements.txt` — Python dependencies
- `runtime.txt` — Python runtime specification for deployment

## License

MIT
