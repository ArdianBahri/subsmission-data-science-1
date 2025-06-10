import joblib
import pandas as pd

# Load pipeline lengkap
pipeline = joblib.load('attrition_pipeline.pkl')

# Data input mentah dari user
data = {
    'Age': [35],
    'BusinessTravel': ['Travel_Rarely'],
    'DailyRate': [800],
    'Department': ['Research & Development'],
    'DistanceFromHome': [5],
    'Education': [3],
    'EducationField': ['Medical'],
    'EnvironmentSatisfaction': [3],
    'Gender': ['Male'],
    'HourlyRate': [60],
    'JobInvolvement': [3],
    'JobLevel': [2],
    'JobRole': ['Research Scientist'],
    'JobSatisfaction': [4],
    'MaritalStatus': ['Single'],
    'MonthlyIncome': [7000],
    'MonthlyRate': [14000],
    'NumCompaniesWorked': [2],
    'OverTime': ['Yes'],
    'PercentSalaryHike': [14],
    'PerformanceRating': [3],
    'RelationshipSatisfaction': [3],
    'StockOptionLevel': [1],
    'TotalWorkingYears': [10],
    'TrainingTimesLastYear': [3],
    'WorkLifeBalance': [3],
    'YearsAtCompany': [5],
    'YearsInCurrentRole': [3],
    'YearsSinceLastPromotion': [2],
    'YearsWithCurrManager': [3],
}

df = pd.DataFrame(data)

# Prediksi langsung (pipeline sudah preprocessing)
pred = pipeline.predict(df)[0]
proba = pipeline.predict_proba(df)[0]

print("\n📊 HASIL PREDIKSI:")
print("-" * 60)
print(f"Status Prediksi             : {'AKAN KELUAR' if pred == 1 else 'TIDAK AKAN keluar'}")
print(f"Tingkat Risiko              : {'TINGGI' if pred == 1 else 'RENDAH'}")
print(f"Probabilitas Bertahan       : {proba[0]*100:.2f}%")
print(f"Probabilitas Akan Keluar    : {proba[1]*100:.2f}%")
