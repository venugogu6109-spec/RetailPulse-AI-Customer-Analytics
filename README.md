# RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

RetailPulse is an end-to-end retail analytics project developed to help retail businesses make smarter decisions using **data analytics, machine learning, demand forecasting, customer segmentation, churn prediction, inventory optimization, and monitoring**.

This project was built as part of my internship/project work and demonstrates how retail transaction data can be transformed into actionable business insights through a complete analytics pipeline and an interactive dashboard.

---

## 📌 Project Objective

The goal of RetailPulse is to build an AI-powered platform that can:

- Analyze retail transaction data
- Segment customers using RFM analysis
- Forecast sales demand using Prophet and LSTM
- Predict customer churn using machine learning
- Optimize inventory planning using forecasted demand
- Monitor data drift and trigger retraining when needed
- Present all insights through a multi-page Streamlit dashboard

---

## 🚀 Key Features

### 1. Data Cleaning & Feature Engineering
- Handled missing values and invalid records
- Converted invoice dates into proper datetime format
- Created useful features such as total transaction value and time-based attributes

### 2. Customer Segmentation
- Performed **RFM (Recency, Frequency, Monetary)** analysis
- Applied **KMeans clustering**
- Grouped customers into business-friendly segments such as:
  - VIP
  - Loyal
  - Regular
  - At Risk

### 3. Demand Forecasting
- Built time-series sales forecasting using:
  - **Prophet**
  - **LSTM**
  - **Hybrid Forecasting Model**
- Generated historical and future demand predictions

### 4. Customer Churn Prediction
- Built a churn prediction model using machine learning
- Performed model evaluation and feature importance analysis
- Used **SHAP** for model explainability

### 5. Inventory Optimization
- Estimated required stock, reorder quantity, and inventory status
- Linked inventory recommendations with forecasted demand

### 6. Monitoring & Retraining
- Added **data drift monitoring**
- Implemented retraining trigger logic when drift exceeds threshold
- Saved retraining logs and metrics

### 7. Streamlit Dashboard
- Built a multi-page interactive dashboard for:
  - Forecasting
  - Segmentation
  - Churn Analysis
  - Inventory Optimization
  - Monitoring

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries / Frameworks
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Prophet
- TensorFlow / Keras
- SHAP
- Optuna
- Streamlit
- Joblib

### Tools / Environment
- Google Colab
- Google Drive
- GitHub

---

## 📂 Project Structure

```bash
RetailPulse_Final_Submission/
│
├── Code/                         # Colab notebooks / project source code
├── Dashboard/                    # Streamlit dashboard files
│   ├── app.py
│   └── pages/
│       ├── 1_Forecasting.py
│       ├── 2_Segmentation.py
│       ├── 3_Churn.py
│       ├── 4_Inventory.py
│       └── 5_Monitoring.py
│
├── Outputs/                      # Generated CSVs, plots, and model files
│   ├── clean_retail_data.csv
│   ├── customer_segments.csv
│   ├── customer_churn_improved.csv
│   ├── sales_forecast.csv
│   ├── future_30_days_forecast.csv
│   ├── hybrid_forecast.csv
│   ├── inventory_optimization.csv
│   ├── drift_summary_day12.csv
│   ├── retraining_log_day13.csv
│   ├── retraining_metrics_day13.csv
│   ├── retrained_churn_model.pkl
│   ├── sales_forecast.png
│   ├── forecast_components.png
│   ├── HybridForecast.png
│   ├── SHAP_Summary.png
│   └── elbow_method.png
│
├── Report/                       # Final project report
├── Demo/                         # Demo notes / video related files
├── README.md
└── requirements.txt
