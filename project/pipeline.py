import pandas as pd
from sqlalchemy import create_engine

def extract_data(file_path):
    """Load data from a local JSON file."""
    with open(file_path, 'r') as file:
        data = pd.read_json(file, orient='records')
    return data

def transform_data(df):
    """Process and clean the data."""
    # Example transformation: Normalize nested JSON columns, handle missing values, etc.
    # If JSON structure is complex, use json_normalize
    if 'nested_column' in df.columns:
        df = pd.json_normalize(df['nested_column'])  # Adjust as needed for actual data structure

    # Fill missing values or perform type conversions
    df.fillna(0, inplace=True)  # Adjust as necessary
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Parse dates if applicable
    return df

def load_data(df, db_connection_string):
    """Load data into a database."""
    engine = create_engine(db_connection_string)
    with engine.connect() as connection:
        df.to_sql('air_quality_data', con=connection, if_exists='replace', index=False)
    print("Data loaded successfully.")

def main():
    # Specify the path to your local JSON file
    file_path = 'path_to_your_file/aqs_api_specification.json'
    
    # Extract data
    df = extract_data(file_path)

    # Transform data
    df = transform_data(df)

    # Load data
    db_connection_string = "sqlite:///air_quality.db"  # Use your database connection string
    load_data(df, db_connection_string)

if __name__ == "__main__":
    main()
