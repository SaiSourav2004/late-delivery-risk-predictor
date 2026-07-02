# 📦 Predicting Late Delivery Risk in E-Commerce Supply Chains

## 📌 Project Overview

In the modern e-commerce landscape, efficient logistics and supply chain management are critical to maintaining customer satisfaction and operational profitability. This project provides a Machine Learning-driven solution to identify and predict the risk of late deliveries before an order is shipped. The solution includes an end-to-end ML pipeline, from data preprocessing and model development to a business-friendly Streamlit deployment.

---

## 🏢 Business Problem

Delivery delays are a major challenge in e-commerce supply chains, directly affecting customer satisfaction, brand reputation, and overall business performance. Unanticipated delays often result in increased customer service costs, refunds, operational inefficiencies, and reduced customer retention.

---

## 🎯 Project Objectives

- Predict the probability of a late delivery using Machine Learning.
- Identify high-risk orders before shipment.
- Support proactive logistics planning and customer communication.
- Provide a user-friendly Streamlit dashboard for business users.
- Demonstrate an end-to-end Data Science workflow from EDA to deployment.

---

## 📊 Dataset Information

**Dataset:** DataCo Smart Supply Chain Dataset

| Attribute | Value |
|------------|--------|
| Records | 180,519 |
| Features Used for Modeling | 24 |
| Problem Type | Binary Classification |
| Target Variable | Late_delivery_risk |

### Key Features

- Shipping Mode
- Customer Segment
- Customer Country
- Department Name
- Category Name
- Order Region
- Market
- Product Price
- Order Quantity
- Benefit per Order
- Sales per Customer
- Order Item Total
- Latitude & Longitude

---

## 🛠️ Technology Stack

### Programming
- Python

### Data Analysis
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-Learn

### Model Serialization
- Joblib

### Deployment
- Streamlit

---

## ⚙️ Machine Learning Workflow

### 1. Data Cleaning
- Removed irrelevant and leakage-prone columns
- Removed operational fields unavailable at prediction time

### 2. Missing Value Handling
- Treated missing values using appropriate preprocessing techniques

### 3. Outlier Treatment
- Analyzed and handled outliers in financial and sales-related variables

### 4. Feature Engineering
- One-Hot Encoding for categorical variables
- Standardization of numerical variables
- ColumnTransformer pipeline implementation

### 5. Feature Selection
- Applied SelectKBest for feature importance analysis

### 6. Train-Test Split
- Stratified Train-Test Split
- Preserved class distribution

### 7. Model Building

The following algorithms were trained and evaluated:

- K-Nearest Neighbors (KNN)
- Gaussian Naive Bayes
- Decision Tree Classifier

### 8. Hyperparameter Tuning

- RandomizedSearchCV
- Tree depth optimization
- Split criteria tuning
- Regularization tuning

### 9. Model Evaluation

Evaluation Metrics:

- Accuracy
- Confusion Matrix
- Classification Report
- ROC-AUC Score

### 10. Deployment

- Model exported using Joblib
- Streamlit application developed for real-time prediction

---

## 🤖 Models Evaluated

| Model | Test Accuracy |
|---------|--------------|
| K-Nearest Neighbors (KNN) | ~63% |
| Gaussian Naive Bayes | ~58% |
| Decision Tree (Baseline) | ~75% |
| Decision Tree (Tuned) | ~71% |

---

## 🏆 Final Model Selection

The baseline Decision Tree model achieved the highest test accuracy and demonstrated strong predictive performance on unseen data.

Although the tuned model reduced overfitting, its test accuracy was lower than the baseline model. Therefore, the baseline Decision Tree was selected as the final deployed model for this academic project.

---

## 📈 Key Insights

- Shipping Mode significantly influences delivery risk.
- Geographic location (Latitude & Longitude) contributes to prediction performance.
- Order profitability and sales-related variables impact delivery outcomes.
- Different markets and regions exhibit varying delivery risk patterns.

---

## 💡 Business Recommendations

### 🔴 High Risk Orders

Recommended Actions:

- Prioritize shipment processing
- Monitor logistics operations closely
- Communicate proactively with customers
- Review delivery routes and operational bottlenecks

### 🟡 Medium Risk Orders

Recommended Actions:

- Monitor warehouse processing timelines
- Ensure timely dispatch
- Track order progress proactively

### 🟢 Low Risk Orders

Recommended Actions:

- Continue standard logistics operations
- Maintain regular shipment monitoring

---

## 🖥️ Streamlit Deployment

A business-friendly Streamlit dashboard was developed to demonstrate real-time delivery risk prediction.

### Features

- User-friendly business interface
- Real-time predictions
- Risk probability estimation
- Executive summary generation
- Operational recommendations
- Automated handling of technical model inputs

---

## 📁 Project Structure

```text
dataco-late-delivery-risk-prediction/
│
├── DataCo_Late_Delivery_Risk_Prediction.ipynb
├── DataCoSupplyChainDataset.csv
├── app.py
├── requirements.txt
├── README.md
├── late_delivery_model.pkl
├── preprocessor.pkl
└── .gitignore
```

---

## 🚀 Installation & Setup

### Clone Repository

```bash
git clone https://github.com/your-username/dataco-late-delivery-risk-prediction.git
cd dataco-late-delivery-risk-prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 🔮 Future Improvements

- Random Forest Implementation
- XGBoost Implementation
- Advanced Feature Engineering
- Feature Correlation Reduction
- MLOps Monitoring
- Data Drift Detection
- Docker Containerization
- AWS Deployment
- Hugging Face Spaces Deployment

---

## 👨‍💻 Author

**Sai Sourav Panigrahi**

Data Science Program – Innomatics Research Labs  
Batch: 501

### Connect With Me

- LinkedIn: Add Your LinkedIn URL
- GitHub: Add Your GitHub URL

---

⭐ If you found this project useful, consider giving it a star on GitHub.