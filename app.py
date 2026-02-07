import streamlit as st
import joblib
import pandas as pd
import numpy as np

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Server CPU Thermal Intelligence System",
    layout="centered"
)

st.title("Server CPU Thermal Intelligence Dashboard")
st.write("Predict CPU temperature and generate proactive cooling recommendations.")

# -------------------------------
# Load Trained Model
# -------------------------------
model = joblib.load("models/server_temp_model.pkl")

# -------------------------------
# User Inputs
# -------------------------------
st.subheader("Input Server Parameters")

cpu_usage = st.slider("CPU Usage (%)", 0.0, 100.0, 50.0)
cpu_frequency = st.number_input("CPU Frequency (MHz)", 1000.0, 5000.0, 3500.0)
memory_usage = st.slider("Memory Usage (%)", 0.0, 100.0, 40.0)
disk_usage = st.slider("Disk Usage (%)", 0.0, 100.0, 50.0)
process_count = st.number_input("Process Count", 1, 1000, 200)
thread_count = st.number_input("Thread Count", 1, 5000, 2500)
gpu_temp = st.slider("GPU Temperature (°C)", 20.0, 100.0, 40.0)
prev_temp = st.slider("Previous CPU Temperature (°C)", 20.0, 100.0, 50.0)

# -------------------------------
# Derived / Assumed Parameters
# -------------------------------
ambient_temp = 25
voltage = 12
current_load = cpu_usage * 0.1

# -------------------------------
# Create Input DataFrame
# -------------------------------
input_data = pd.DataFrame([[  
    cpu_usage,
    cpu_frequency,
    memory_usage,
    disk_usage,
    process_count,
    thread_count,
    gpu_temp,
    ambient_temp,
    voltage,
    current_load,
    prev_temp
]], columns=[
    'CPU_Usage',
    'CPU_Frequency',
    'Memory_Usage',
    'Disk_Usage',
    'Process_Count',
    'Thread_Count',
    'GPU_Temperature',
    'Ambient_Temperature',
    'Voltage',
    'Current_Load',
    'Prev_CPU_Temperature'
])

# -------------------------------
# Prediction & Recommendation
# -------------------------------
if st.button("Run Thermal Analysis"):

    prediction = model.predict(input_data)[0]

    st.subheader("Predicted Temperature")
    st.metric(label="CPU Temperature (°C)", value=f"{prediction:.2f}")

    # Thresholds
    SAFE_THRESHOLD = 75
    CRITICAL_THRESHOLD = 85

    st.subheader("Thermal Risk Assessment")

    if prediction < SAFE_THRESHOLD:
        st.success("Status: SAFE")
        st.write("Cooling Recommendation: Normal airflow is sufficient.")

    elif SAFE_THRESHOLD <= prediction < CRITICAL_THRESHOLD:
        st.warning("Status: HIGH LOAD")
        st.write("Cooling Recommendation: Increase fan speed to 60–70% and monitor temperature closely.")

    else:
        st.error("Status: CRITICAL OVERHEAT RISK")
        st.write("Cooling Recommendation: Activate secondary cooling and reduce CPU frequency immediately.")

    # Cooling Demand Score
    cooling_demand = prediction - SAFE_THRESHOLD
    normalized_score = min(max(int((cooling_demand / 20) * 100), 0), 100)

    st.subheader("Cooling Demand Indicator")
    st.progress(normalized_score)

    st.caption("Cooling Demand Score represents how far the predicted temperature exceeds safe operating limits.")
