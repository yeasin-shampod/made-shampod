import requests
import pandas as pd
from sqlalchemy import create_engine

# Replace with your API key if needed
API_KEY = 'YOUR_API_KEY'
BASE_URL = "https://aqs.epa.gov/data/api"

def fetch_data(endpoint, params):
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(f"{BASE_URL}/{endpoint}", params=params, headers=headers)
    response.raise_for_status()
    return response.json()

def transform_data(json_data):
    # Extract data from JSON
    records = json_data.get('Data', [])
    # Normalize data into DataFrame
    df = pd.json_normalize(records)
    # Handle missing values or transformations if needed
    df.fillna(0, inplace=True)
    return df

def load_data_to_db(df, db_connection_string):
    engine = create_engine(db_connection_string)
    with engine.connect() as connection:
        df.to_sql('air_quality_data', con=connection, if_exists='append', index=False)
    print("Data loaded successfully.")

def main():
    # Define the parameters for the API call
    params = {
        "param": "44201",  # Example: Ozone parameter code
        "bdate": "20230101",  # Begin date (yyyymmdd)
        "edate": "20231231",  # End date (yyyymmdd)
        "state": "01",  # Example: Alabama state code
        "county": "001"  # Example: Autauga county code
    }
    
    # Fetch data
    json_data = fetch_data("dailyData/byCounty", params)

    # Transform data
    df = transform_data(json_data)

    # Load data
    db_connection_string = "sqlite:///air_quality.db"  # Use your database connection string
    load_data_to_db(df, db_connection_string)

if __name__ == "__main__":
    main()

