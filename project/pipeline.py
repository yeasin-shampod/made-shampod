import pandas as pd
import os
from sqlalchemy import create_engine

# Create a /data directory if it doesn't exist
os.makedirs("/data", exist_ok=True)

def extract_data():
    """Load data from a local JSON file or any other source."""
    file_path = '/path_to_your_data/your_data_file.json'
    data = pd.read_json(file_path)  # Adjust based on your file format
    return data

def transform_data(df):
    """Process and clean the data."""
    # Example transformation: fill missing values, normalize, or convert types
    df.fillna(0, inplace=True)
    return df

def load_data(df):
    """Load data into a SQLite database."""
    db_path = '/data/air_quality_data.db'
    engine = create_engine(f'sqlite:///{db_path}')
    with engine.connect() as connection:
        df.to_sql('air_quality_data', con=connection, if_exists='replace', index=False)
    print("Data loaded successfully into /data/air_quality_data.db.")

def main():
    # Extract
    df = extract_data()

    # Transform
    df = transform_data(df)

    # Load
    load_data(df)

if __name__ == "__main__":
    main()
