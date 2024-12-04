import pandas as pd
import sqlite3

# Step 1: Extract function to load data from URLs
def extract_data():
    # URLs for datasets
    url1 = "https://data.wprdc.org/datastore/dump/967f1285-f8fb-4785-9673-64a8ae47588d"
    url2 = "https://data.cityofnewyork.us/api/views/c3uy-2p5r/rows.csv?accessType=DOWNLOAD"
    
    # Load data from URLs into pandas DataFrames
    df1 = pd.read_csv(url1)
    df2 = pd.read_csv(url2)

    print("Data extracted successfully.")
    print(len(df1.index))
    print(len(df2.index))
    return df1, df2

# Step 2: Transform function to clean and process data
def transform_data(df1, df2):
    # Clean df1 columns
    df1.columns = [col.lower().replace(' ', '_') for col in df1.columns]
    
    # Handle missing values or unwanted text
    df1.dropna(subset=['black_carbon', 'pm25'], inplace=True)  # Drop rows with missing key columns
    df1['datetime'] = pd.to_datetime(df1['datetime'], errors='coerce')  # Ensure datetime format

    # Clean df2 columns
    df2.columns = [col.lower().replace(' ', '_') for col in df2.columns]

    # Transform start_date to datetime and handle missing values
    df2['start_date'] = pd.to_datetime(df2['start_date'], errors='coerce')
    df2.fillna({'data_value': 0}, inplace=True)  # Fill missing values in df2's 'data_value' column

    print("Data transformed successfully.")
    return df1, df2

# Step 3: Load function to save data into CSV files and SQLite databases
def load_data(df1, df2):
    # Save df1 as CSV file in /data directory
    df1.to_csv('data/dataset_1.csv', index=False)

    # Save df2 as CSV file in /data directory
    df2.to_csv('data/dataset_2.csv', index=False)

    # Save df1 to SQLite database (dataset_1.db)
    conn1 = sqlite3.connect('data/dataset_1.db')
    df1.to_sql('dataset_1', conn1, if_exists='replace', index=False)
    conn1.commit()
    conn1.close()

    # Save df2 to SQLite database (dataset_2.db)
    conn2 = sqlite3.connect('data/dataset_2.db')
    df2.to_sql('dataset_2', conn2, if_exists='replace', index=False)
    conn2.commit()
    conn2.close()

    print("Data loaded into CSV and SQLite databases successfully.")

if __name__ == '__main__':
    # Execute ETL process
    df1, df2 = extract_data()   # Extract data
    df1, df2 = transform_data(df1, df2)   # Transform data
    load_data(df1, df2)  # Load data into CSV and SQLite

    print("ETL process completed successfully.")
