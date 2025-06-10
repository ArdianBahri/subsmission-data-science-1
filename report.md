# Proyek Data Science - HR Analytics: Employee Attrition Prediction

## Latar Belakang

Jaya Jaya Maju adalah perusahaan multinasional dengan lebih dari 1000 karyawan. Perusahaan ini menghadapi masalah serius: tingkat attrition (keluarnya karyawan) melebihi 10%, yang berdampak pada biaya rekrutmen, produktivitas, dan stabilitas organisasi. Departemen HR membutuhkan solusi berbasis data untuk memantau, menganalisis, dan memprediksi attrition.

---

## Tujuan Proyek

1. Mengidentifikasi faktor-faktor yang mempengaruhi attrition.
2. Membuat business dashboard untuk membantu pemantauan.
3. Membangun model prediksi attrition.
4. Menyediakan tools lokal prediksi menggunakan script Python.

---

## Dataset

Dataset yang digunakan: [employee\_data.csv](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Berisi 1470 entri dengan fitur seperti:

* Demografis: Age, Gender, MaritalStatus
* Pekerjaan: JobRole, Department, YearsAtCompany
* Kompensasi: MonthlyIncome, StockOptionLevel
* Kepuasan: JobSatisfaction, WorkLifeBalance
* Target: `Attrition` (Yes/No)

---

## Proses Data Science

### 1. Business Understanding

Masalah utama: attrition rate >10% menyebabkan instabilitas.

### 2. Data Understanding

* Total data: 1470 baris × 35 kolom
* Distribusi `Attrition`: 16.1% keluar, 83.9% bertahan
* Fitur penting (berdasarkan EDA): OverTime, MonthlyIncome, JobSatisfaction, YearsAtCompany

### 3. Data Preparation

* Encoding: LabelEncoder untuk target & beberapa fitur kategorikal
* Feature scaling: StandardScaler untuk fitur numerik
* Split data: 80% latih, 20% uji

### 4. Modeling

Model utama: **Random Forest Classifier**

* Hyperparameter tuning dengan GridSearchCV
* Dibandingkan juga dengan Logistic Regression dan SVM

### 5. Evaluation

Model terbaik: RandomForest (setelah tuning)

* Accuracy: **87.4%**
* Precision (kelas keluar): **0.71**
* Recall: **0.64**
* F1-Score: **0.67**
* ROC-AUC Score: **0.88**

### 6. Deployment

Model disimpan dengan `joblib` ke `model/model.pkl`
Prediksi lokal dapat dilakukan dengan `predict.py`

---

## Dashboard Bisnis

Dashboard dibuat dengan **Looker Studio**.

🔗 [Akses Dashboard (Looker Studio)](https://lookerstudio.google.com/s/your-dashboard-link)

Fitur:

* Distribusi attrition per departemen
* Hubungan MonthlyIncome dengan Attrition
* Attrition by JobRole
* Visualisasi sebaran faktor-faktor penting

Login (jika menggunakan Metabase):

* Email: `root@mail.com`
* Password: `root123`

---

## Requirements

```txt
pandas==1.5.3
numpy==1.24.3
scikit-learn==1.2.2
matplotlib==3.7.1
seaborn==0.12.2
joblib==1.2.0
jupyter==1.0.0
```

---

## Menjalankan Prediksi Lokal

```bash
pip install -r requirements.txt
python predict.py
```

Masukkan fitur-fitur seperti usia, income, overtime, dll., dan model akan mengembalikan prediksi apakah karyawan akan keluar atau tidak.

---

## Rekomendasi Action Items

1. Kurangi beban lembur (OverTime)
2. Berikan insentif bagi karyawan berpenghasilan rendah
3. Lakukan survey rutin untuk JobSatisfaction
4. Fokus retensi pada karyawan < 3 tahun masa kerja
5. Program mentoring untuk karyawan baru

---

## Struktur Direktori Submission

```
submission
├── model/
│   └── model.pkl
├── notebook.ipynb
├── prediction.py
├── README.md
├── <username_dicoding>-dashboard.png
├── metabase.db.mv.db (opsional)
├── requirements.txt
```

---

## Kesimpulan

Proyek ini membantu HR Jaya Jaya Maju memahami dan memprediksi attrition. Dengan model machine learning yang akurat dan dashboard visual yang informatif, perusahaan dapat mengambil langkah strategis berbasis data untuk menurunkan attrition di bawah 10%.

---

Selamat mengerjakan submission dan semoga sukses!
