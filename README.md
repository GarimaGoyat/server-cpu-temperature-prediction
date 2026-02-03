
# Server CPU Temperature Prediction

## 📌 Problem Statement

Large-scale computing infrastructure such as cloud data centers face overheating risks due to high workloads and environmental conditions. Predicting server CPU temperature in advance can help in proactive cooling management and failure prevention.

This project builds a supervised machine learning regression model to estimate CPU temperature based on system workload and environmental parameters.

---

## 📊 Input Features

- CPU Utilization (%)
- Memory Usage (%)
- Clock Speed (GHz)
- Ambient Temperature (°C)
- Voltage (V)
- Current Load (A)

## 🎯 Target Variable

- CPU Temperature (°C)

---

## 🛠️ Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn

---

## ⚙️ Project Workflow

1. Dataset creation and preprocessing
2. Feature scaling and data splitting
3. Model training using regression algorithms
4. Model evaluation using MAE, RMSE, and R² score
5. Temperature risk classification for proactive cooling decisions

---

## 📈 Machine Learning Models

- Linear Regression
- Random Forest Regressor

---

## 🚨 Proactive Cooling Logic

- **Safe**: Temperature < 70°C
- **Moderate Risk**: 70–80°C
- **High Risk**: > 80°C

---

## 📁 Project Structureserver-cpu-temperature-prediction/

│
├── data/
│   └── server_temperature_data.csv
│
├── model/
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── notebooks/
│   └── exploration.ipynb
│
├── results/
│   └── metrics.txt
│
├── README.md
└── requirements.txt


## 🔮 Future Scope


- Real-time server monitoring integration
- Deep learning-based temperature prediction
- Cloud deployment and API integration
