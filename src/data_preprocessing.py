import pandas as pd

def clean_data(df):
    """
    Cleans the server CPU dataset by handling missing values 
    and removing physical anomalies.
    """
    # 1. Drop rows where the target (CPU_Temperature) is missing
    df = df.dropna(subset=['CPU_Temperature'])
    
    # 2. Fill missing features with the mean to maintain data volume
    df['Memory_Usage'] = df['Memory_Usage'].fillna(df['Memory_Usage'].mean())
    df['CPU_Frequency'] = df['CPU_Frequency'].fillna(df['CPU_Frequency'].mean())
    
    # 3. Remove outliers (impossible sensor readings)
    # Keeping temperatures between 20°C and 100°C
    df = df[(df['CPU_Temperature'] >= 20) & (df['CPU_Temperature'] <= 100)]
    
    # 4. Filter for only the features needed for the AI
    required_columns = [
        'CPU_Usage', 'CPU_Frequency', 'Memory_Usage', 
        'Process_Count', 'Thread_Count', 'CPU_Temperature'
    ]
    df = df[required_columns]
    
    return df

if __name__ == "__main__":
    # Change '../data/...' to 'data/...' because we are running from the main folder
    try:
        raw_data = pd.read_csv('data/server_temperature_data.csv') 
        cleaned_df = clean_data(raw_data)
        print(f"Cleaning complete. Remaining rows: {len(cleaned_df)}")
        
        # Save the result so the team can use it
        cleaned_df.to_csv('data/cleaned_server_data.csv', index=False)
        print("File saved as 'data/cleaned_server_data.csv'")
        
    except FileNotFoundError:
        print("Error: Could not find the CSV file. Check your folder path!")