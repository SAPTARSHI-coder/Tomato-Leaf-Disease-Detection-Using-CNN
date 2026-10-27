# Tomato Leaf Disease Detection System

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow / Keras](https://img.shields.io/badge/Framework-TensorFlow%20%7C%20Keras-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Flask](https://img.shields.io/badge/App-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://palletsprojects.com/p/flask/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

An intelligent computer vision system for automated detection and diagnosis of tomato leaf diseases using Convolutional Neural Networks (CNN) and Transfer Learning (EfficientNetB0). Features a complete model training workflow, evaluation metrics, and a responsive Flask web application for interactive classification.

---

## 📌 Project Overview

Tomato crops are susceptible to numerous fungal, bacterial, and viral foliar diseases that can severely impact agricultural yields. Early and accurate detection allows farmers to administer targeted treatments before widespread crop damage occurs.

This project delivers:
- **Binary & Multi-class Detection**: Distinguishes between healthy tomato leaves and diseased specimens.
- **Deep Learning Pipelines**: Preprocessing, augmentation, model training, and checkpointing (`best_model.h5`).
- **Interactive Web Interface**: A modern Flask-powered web application allowing users to upload leaf photos for immediate diagnosis and confidence scores.
- **Comprehensive Academic Report**: Complete documentation including formal LaTeX reports, methodology breakdowns, and presentations.

---

## 🔬 Dataset & Preprocessing

The model is trained on curated agricultural imagery divided into structured training and evaluation sets:
- **Image Preprocessing**: Resizing to $224 \times 224$, standard RGB normalization, and data augmentation (rotations, horizontal flips, zoom).
- **Split Configuration**: Automated dataset splitting via `split_dataset.py` into stratified training and testing partitions (`dataset/` and `dataset_binary/`).

---

## 🏗️ Architecture & Model Pipeline

1. **Backbone**: EfficientNetB0 / Custom Convolutional Backbone with Transfer Learning.
2. **Dense Head**: Global Average Pooling $\rightarrow$ Dense layers with Batch Normalization and Dropout $\rightarrow$ Softmax/Sigmoid classification output.
3. **Loss & Optimizer**: Binary/Categorical Cross-entropy optimized via Adam with learning-rate scheduling and Early Stopping.

---

## 🚀 Quickstart Guide

### 1. Installation & Environment Setup

```bash
# Clone the repository
git clone https://github.com/SAPTARSHI-coder/Tomato-Leaf-Disease-Detection-Using-CNN.git
cd Tomato-Leaf-Disease-Detection-Using-CNN

# Install required dependencies
pip install tensorflow keras flask werkzeug pillow matplotlib numpy
```

### 2. Launch the Flask Web Dashboard

```bash
python app.py
```
Open your browser and navigate to `http://localhost:5000` to access the interactive diagnosis interface.

### 3. Run Inference from CLI

```bash
python predict.py --image path/to/leaf_image.jpg
```

### 4. Retrain or Evaluate the Model

```bash
python train_model.py
```
Training telemetry and accuracy graphs will be exported to `final_graph.png` and `training_results.json`.

---

## 📁 Repository Structure

```
├── app.py                      # Flask web application & diagnosis API
├── predict.py                  # Standalone inference & classification module
├── train_model.py              # CNN model training and validation workflow
├── convert_binary.py           # Utility to organize binary classification sets
├── split_dataset.py            # Train/validation/test split generation
├── graph.py                    # Loss & accuracy curve visualization generator
├── training_results.json       # Serialized metrics and training telemetry
├── final_graph.png             # Performance visual plots
├── dataset/                    # Dataset directory
├── templates/                  # Frontend HTML/CSS templates for web app
└── Tomato_Leaf_Disease_Report.*# Formal LaTeX and PDF academic reports
```

---

## 👨‍💻 Author

**Saptarshi Sadhu**
- Website: [saptarshisadhu.co.in](https://saptarshisadhu.co.in/)
- GitHub: [@SAPTARSHI-coder](https://github.com/SAPTARSHI-coder)
- LinkedIn: [in/saptarshi-sadhu](https://www.linkedin.com/in/saptarshi-sadhu/)
