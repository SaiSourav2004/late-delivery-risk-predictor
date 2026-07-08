# 🚚 Late Delivery Risk Prediction in Supply Chain Operations

### End-to-End Machine Learning Project | Classification | Streamlit Deployment | Business Analytics

Predict delivery delays before shipment using Machine Learning and help logistics teams make proactive, data-driven decisions.

---

## 🌍 Business Problem

In today's e-commerce ecosystem, customers expect fast and reliable deliveries. However, unexpected shipment delays can lead to:

- Reduced customer satisfaction
- Increased operational costs
- Negative brand perception
- Customer churn and revenue loss

Organizations often react to delays after they occur.

This project focuses on predicting **Late Delivery Risk** before shipment, enabling businesses to take preventive actions and improve logistics performance.

---

## 🎯 Project Goal

Build a Machine Learning system capable of predicting whether an order will be delivered:

✅ On Time

❌ Late

The solution helps logistics teams identify high-risk shipments early and improve operational planning.

---

## 📊 Dataset Overview

**Dataset:** DataCo Smart Supply Chain Dataset

| Attribute | Value |
|------------|--------|
| Records | 180,519 |
| Original Features | 53 |
| Numerical Features | 14 |
| Categorical Features | 10 |
| Problem Type | Binary Classification |
| Target Variable | `Late_delivery_risk` |

### Target Classes

| Value | Meaning |
|---------|---------|
| 0 | On-Time Delivery |
| 1 | Late Delivery |

---

# 🏗️ Project Architecture

```text
Raw Supply Chain Data
          │
          ▼
Data Understanding
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Train-Test Split
          │
          ▼
Data Preprocessing
 ├── RobustScaler
 └── OneHotEncoder
          │
          ▼
Feature Selection
          │
          ▼
Model Training
 ├── KNN
 ├── Gaussian Naive Bayes
 └── Decision Tree
          │
          ▼
Hyperparameter Tuning
          │
          ▼
Model Evaluation
          │
          ▼
Streamlit Deployment
```

---

# 🔍 Exploratory Data Analysis

EDA was performed to understand delivery behavior and uncover business insights.

### Key Findings

📦 Shipping mode significantly influences delivery performance.

🌎 Geographic location plays an important role in delivery risk.

💰 Profit and sales-related variables impact shipment outcomes.

📈 Certain features show strong relationships with delivery delays.

---

# ⚙️ Data Preprocessing

To ensure reliable model performance, a complete preprocessing pipeline was developed.

### Numerical Features

Applied:

- RobustScaler

Why?

- Resistant to outliers
- Uses Median and IQR
- Suitable for real-world business data

### Categorical Features

Applied:

- OneHotEncoder

Why?

- Prevents false ordinal relationships
- Handles nominal categories effectively

### Pipeline

Implemented using:

```python
ColumnTransformer
```

Final transformed dataset:

```python
Train Shape : (144415, 325)

Test Shape  : (36104, 325)
```

---

# 🎯 Feature Selection

Feature Selection was performed using:

```python
SelectKBest(score_func=mutual_info_classif)
```

### Most Important Features

- Latitude
- Longitude
- Shipping Mode
- Benefit per Order
- Order Profit Per Order
- Sales per Customer
- Order Item Total

This step helped improve model efficiency and interpretability.

---

# 🤖 Machine Learning Models

The following classification algorithms were trained and evaluated:

| Model | Description |
|---------|-------------|
| K-Nearest Neighbors | Distance-based classifier |
| Gaussian Naive Bayes | Probabilistic classifier |
| Decision Tree | Rule-based classifier |

---

# ⚡ Hyperparameter Tuning

To improve model performance and reduce overfitting, hyperparameter tuning was performed using:

```python
RandomizedSearchCV
```

### Best Parameters

```python
max_depth = 25

min_samples_split = 5

min_samples_leaf = 2
```

---

# 🏆 Final Model Performance

### Best Model: Decision Tree Classifier

| Metric | Score |
|----------|----------|
| Accuracy | 75.46% |
| ROC-AUC Score | 0.7553 |
| Precision | 0.78 |
| Recall | 0.78 |
| F1 Score | 0.78 |

---

# 📈 Confusion Matrix

| Actual / Predicted | On-Time | Late |
|-------------------|----------|---------|
| On-Time | 11846 | 4462 |
| Late | 4399 | 15397 |

---

# 💡 Business Impact

The model can help organizations:

✅ Identify high-risk deliveries before shipment

✅ Improve logistics planning

✅ Reduce customer complaints

✅ Optimize shipment prioritization

✅ Improve operational efficiency

✅ Support data-driven supply chain decisions

---

# 🚀 Live Application

A production-ready Streamlit application was developed to demonstrate real-time predictions.

### Features

- Real-Time Predictions
- Interactive Dashboard
- Automated Preprocessing
- User-Friendly Interface
- Instant Delivery Risk Assessment

### Live Demo

🔗 https://late-delivery-risk-predictor-6iyq2e2lchacb4p6uibmk5.streamlit.app/

---

# 🛠️ Technology Stack

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-Learn

### Deployment

- Streamlit

### Model Serialization

- Joblib

---

# 📂 Repository Structure

```text
Late-Delivery-Risk-Prediction/
│
├── notebook/
│   └── DataCo_Late_Delivery_Risk_Prediction.ipynb
│
├── app.py
├── requirements.txt
├── late_delivery_model.pkl
├── preprocessor.pkl
├── README.md
└── assets/
```

---

# 🔮 Future Enhancements

- Random Forest & XGBoost Models
- Real-Time Shipment Tracking Integration
- Automated Model Monitoring
- Docker Containerization
- Cloud Deployment (AWS/Azure)
- MLOps Pipeline Integration

---

# 👨‍💻 About Me

### Sai Sourav Panigrahi

Aspiring Data Scientist passionate about solving real-world business problems using Machine Learning, Data Analytics, and AI.

### Connect With Me

🔗 LinkedIn  
https://www.linkedin.com/in/saisourav-panigrahi/

🔗 GitHub  
https://github.com/SaiSourav2004

---

### ⭐ If you found this project valuable, consider giving the repository a star.
