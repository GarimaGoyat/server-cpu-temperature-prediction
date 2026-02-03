import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
from data_preprocessing import clean_data

# 1. Load Data
df_raw = pd.read_csv('data/server_temperature_data.csv')
df = clean_data(df_raw)

# 2. Setup Features and Target
X = df[['CPU_Usage', 'CPU_Frequency', 'Memory_Usage', 'Process_Count', 'Thread_Count']]
y = df['CPU_Temperature']

# 3. Train the AI
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Create the models folder if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# 5. Save the "Brain" and Print Success
joblib.dump(model, 'models/server_temp_model.pkl')
print("✅ SUCCESS: The model has been trained and saved to models/server_temp_model.pkl")