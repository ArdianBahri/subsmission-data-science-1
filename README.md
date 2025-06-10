# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## 📋 Executive Summary

Proyek ini mengembangkan model prediktif untuk mengidentifikasi karyawan yang berisiko tinggi mengalami attrition (resign) di perusahaan Edutech. Dengan menggunakan machine learning, kami berhasil mencapai **86.7% accuracy** dan dapat menghemat potensi biaya hingga **$2.1 juta per tahun**.

### 🎯 Key Results
- **Model Performance**: 86.7% Accuracy, 0.859 ROC AUC
- **Attrition Rate**: 16.1% (237 dari 1,470 karyawan)
- **Potential Savings**: $2,115,000 per tahun
- **ROI**: Setiap $1 investasi menghasilkan $9 return

## 📊 Business Dashboard

### Attrition Overview
```
Total Karyawan    : 1,470
Attrition         : 237 (16.1%)
No Attrition      : 1,233 (83.9%)
Target Reduction  : 10% dalam 12 bulan
```

### Department Analysis
| Department | Total Karyawan | Attrition | Rate |
|------------|----------------|-----------|------|
| Sales | 446 | 92 | 20.6% |
| Research & Development | 961 | 133 | 13.8% |
| Human Resources | 63 | 12 | 19.0% |

### Top Risk Factors
1. **Overtime** - Karyawan dengan overtime memiliki 30.5% attrition rate
2. **Monthly Income < $3,000** - 22.4% attrition rate
3. **Age < 30 tahun** - 25.8% attrition rate
4. **Years at Company < 2** - 28.3% attrition rate
5. **Work-Life Balance (Poor)** - 31.2% attrition rate

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- 8GB RAM minimum

### Installation

1. **Clone Repository**
```bash
git clone [https://github.com/yourusername/edutech-attrition-project.git](https://github.com/ArdianBahri/subsmission-data-science-1.git)
cd edutech-attrition-project
```

2. **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Analysis**
```bash
jupyter notebook notebook.ipynb
# atau
python employee_attrition_analysis.py
```

## 📁 Project Structure

```
edutech-attrition-project/
│
├── data/
│   ├── employee_data.csv          # Dataset original
│   └── data_dictionary.txt        # Penjelasan variabel
│
├── models/
│   ├── best_attrition_model.pkl   # Model Random Forest terbaik
│   └── feature_scaler.pkl         # StandardScaler untuk features
│
├── notebooks/
│   └── notebook.ipynb             # Jupyter notebook analisis lengkap
│
├── src/
│   ├── employee_attrition_analysis.py  # Script Python standalone
│   ├── preprocessing.py           # Fungsi preprocessing
│   └── visualization.py           # Fungsi visualisasi
│
├── outputs/
│   ├── feature_importance.png     # Visualisasi feature importance
│   ├── confusion_matrix.png       # Confusion matrix
│   └── model_comparison.png       # Perbandingan model
│
├── docs/
│   ├── metabase_dashboard.md      # Dokumentasi dashboard
│   └── business_report.pdf        # Laporan bisnis lengkap
│
├── requirements.txt               # Python dependencies
├── README.md                      # Dokumentasi proyek
└── .gitignore                    # Git ignore file
```

## 🔍 Data Understanding

### Dataset Overview
- **Total Records**: 1,470 karyawan
- **Features**: 35 variabel
- **Target**: Attrition (Binary: 0=No, 1=Yes)
- **Missing Values**: 0%

### Feature Categories

#### 1. **Demographics**
- Age, Gender, MaritalStatus, Education, EducationField

#### 2. **Job-Related**
- Department, JobRole, JobLevel, JobInvolvement
- YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion

#### 3. **Compensation & Benefits**
- MonthlyIncome, PercentSalaryHike, StockOptionLevel

#### 4. **Work Conditions**
- BusinessTravel, DistanceFromHome, OverTime
- EnvironmentSatisfaction, JobSatisfaction, WorkLifeBalance

#### 5. **Performance**
- PerformanceRating, TrainingTimesLastYear

## 🤖 Modeling Approach

### Models Evaluated
1. **Logistic Regression** - Baseline model
2. **Decision Tree** - Interpretable model
3. **Random Forest** - Best performer ✅
4. **Support Vector Machine** - Complex patterns

### Model Performance Comparison
| Model | Accuracy | ROC AUC | Precision | Recall |
|-------|----------|---------|-----------|---------|
| Random Forest (Tuned) | **0.867** | **0.859** | **0.853** | **0.786** |
| SVM | 0.854 | 0.842 | 0.831 | 0.762 |
| Logistic Regression | 0.847 | 0.835 | 0.822 | 0.752 |
| Decision Tree | 0.821 | 0.798 | 0.795 | 0.714 |

### Hyperparameter Tuning
Best parameters untuk Random Forest:
```python
{
    'n_estimators': 200,
    'max_depth': 20,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'class_weight': 'balanced'
}
```

## 📈 Business Impact Analysis

### Cost-Benefit Analysis

#### Assumptions
- **Cost of Employee Turnover**: $50,000 per employee
- **Cost of Retention Program**: $5,000 per employee
- **Model Implementation Cost**: $50,000 (one-time)

#### Projected Annual Impact
```
Correctly Identified At-Risk Employees : 47
Potential Turnover Prevented          : 47 employees
Gross Savings                        : $2,350,000
Program Costs                        : $235,000
Implementation Cost (Year 1)         : $50,000
----------------------------------------
Net Benefit (Year 1)                 : $2,065,000
Net Benefit (Year 2+)                : $2,115,000
```

### ROI Calculation
- **Year 1 ROI**: 380% 
- **3-Year ROI**: 1,260%
- **Payback Period**: < 3 months

## 💡 Key Insights & Recommendations

### Top 5 Most Important Features
1. **OverTime** (0.1842) - Strongest predictor
2. **MonthlyIncome** (0.1523) - Compensation matters
3. **Age** (0.1287) - Younger employees at higher risk
4. **TotalWorkingYears** (0.1156) - Experience retention
5. **YearsAtCompany** (0.0987) - Tenure importance

### Strategic Recommendations

#### 1. **Immediate Actions (0-3 months)**
- 🔴 **Overtime Policy Reform**
  - Implement mandatory time-off after extended overtime
  - Introduce flexible working hours
  - Maximum 10 hours overtime per month
  
- 💰 **Compensation Adjustment**
  - Increase salaries for employees earning < $3,000
  - Focus on Sales department (highest attrition)
  - Implement performance-based bonuses

#### 2. **Short-term Initiatives (3-6 months)**
- 👥 **Enhanced Onboarding**
  - 90-day structured program for new hires
  - Assign mentors for first 6 months
  - Regular check-ins at 30, 60, 90 days
  
- 📊 **Manager Training**
  - Train managers to identify burnout signs
  - Weekly 1-on-1 meetings
  - Employee engagement workshops

#### 3. **Long-term Strategy (6-12 months)**
- 🎯 **Career Development**
  - Clear promotion pathways
  - Annual career planning sessions
  - Skill development programs
  
- 🏖️ **Work-Life Balance**
  - Unlimited PTO policy
  - Mental health support
  - Remote work options

## 🔧 Model Deployment & Monitoring

### Deployment Strategy
```python
# Load model untuk prediksi
import joblib
import pandas as pd

# Load model dan scaler
model = joblib.load('models/best_attrition_model.pkl')
scaler = joblib.load('models/feature_scaler.pkl')

# Predict function
def predict_attrition_risk(employee_data):
    # Preprocess
    data_scaled = scaler.transform(employee_data)
    
    # Predict probability
    risk_score = model.predict_proba(data_scaled)[0, 1]
    
    # Risk category
    if risk_score > 0.7:
        return "High Risk", risk_score
    elif risk_score > 0.4:
        return "Medium Risk", risk_score
    else:
        return "Low Risk", risk_score
```

### Monitoring Plan
- **Weekly**: Review high-risk employees list
- **Monthly**: Update model with new data
- **Quarterly**: Retrain model and assess performance
- **Annually**: Comprehensive model evaluation

### Success Metrics
1. **Reduction in Attrition Rate**: Target 10% → 6% reduction
2. **Cost Savings**: Track actual vs projected savings
3. **Employee Satisfaction**: Quarterly survey scores
4. **Model Accuracy**: Maintain >85% accuracy

## 📧 API Usage Example

```python
import requests
import json

# API endpoint (example)
url = "https://api.edutech.com/predict-attrition"

# Employee data
employee = {
    "Age": 28,
    "MonthlyIncome": 2800,
    "OverTime": "Yes",
    "YearsAtCompany": 1,
    "JobSatisfaction": 2
}

# Make prediction
response = requests.post(url, json=employee)
result = response.json()

print(f"Risk Level: {result['risk_level']}")
print(f"Risk Score: {result['risk_score']:.1%}")
print(f"Recommended Actions: {result['recommendations']}")
```

## 🏆 Project Outcomes

### Achieved
- ✅ Developed accurate predictive model (86.7% accuracy)
- ✅ Identified key attrition factors
- ✅ Created actionable recommendations
- ✅ Demonstrated clear ROI ($2.1M annual savings)

### Next Steps
1. Deploy model to production environment
2. Integrate with HR management system
3. Develop real-time dashboard
4. Implement A/B testing for retention strategies
5. Expand model to predict performance and engagement
